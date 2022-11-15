from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q, Avg
from django.contrib import messages
from checkout.models import Order, OrderLineItem
from .models import Product, Category, Offer, ReviewProduct


def products(request):
    """
    A view to return the All products page,
    Search and sort products funcionality, 
    Category return from nav links.
    """
    products_list = Product.objects.all().order_by("-release_date")
    total_products_list = products_list.count()

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            if sortkey == 'name':
                sortkey = 'lower_name'
                products_list = products_list.annotate(lower_name=Lower('name'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products_list = products_list.order_by(sortkey)

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products_list = products_list.filter(category__system_name__in=categories)
            categories = Category.objects.filter(system_name__in=categories)
            total_products_list = products_list.count()

    if request.GET:
        if 'offer' in request.GET:
            offers = request.GET['offer'].split(',')
            products_list = products_list.filter(offer__offer_name__in=offers)
            offers = Offer.objects.filter(offer_name__in=offers)
            total_products_list = products_list.count()

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products_list = products_list.filter(queries)
            total_products_list = products_list.count()

    paginator = Paginator(products_list, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "products_list": products_list,
        "total_products_list": total_products_list,
        'page_obj': page_obj,
        'paginator': paginator,
    }

    return render(request, 'products/products_all.html', context)


def product_details(request, slug):
    """
    A view to show individual product details and category
    """

    product = get_object_or_404(Product, slug=slug)
    product_review = product.product_review.filter(reviewed=True).order_by("-created_on")
    total_review = product_review.count()
    avg_review = product.product_review.aggregate(review=Avg('review'))['review']

    context = {
        'product': product,
        'product_review': product_review,
        'total_review': total_review,
        'avg_review': avg_review
    }

    return render(request, 'products/product_details.html', context)


@login_required
def review_product(request, slug):
    """
    A view to user review a product
    """
    # Get product and reviews data
    product = get_object_or_404(Product, slug=slug)
    product_review = product.product_review.filter(reviewed=True).order_by("-created_on")
    total_review = product_review.count()
    avg_review = product.product_review.aggregate(review=Avg('review'))['review']
    # Get current user email and id
    current_user_email = request.user.email
    current_user_id = request.user.id
    # Converts product id to int to check against list
    product_str = str(product)
    product_int = int(product_str)
    # One list for all items and another to remove repeats (skus)
    items_list = []
    skus_list = []
    # Checkers. If the user bought the product and has already given his review
    purchased = False
    reviewed = False
    # Takes all the user orders and makes them into a list
    get_user_orders = Order.objects.filter(email=current_user_email)
    order_list = list(get_user_orders)
    # While to check the products inside the orders
    while True:
        if len(order_list) == 0:
            break
        else:
            order = order_list[0]
            get_user_items = OrderLineItem.objects.filter(order=order).values('product_id')
            filter_items = list(get_user_items)
            items_list.append(filter_items)
            order_list.pop(0)
            order = None
            continue
    # For loop into list to get the product skus
    for item_dict in items_list:
        for item in item_dict:
            for i in item.values():
                if i not in skus_list:
                    skus_list.append(i)
    # Condition for Checkers
    if product_review.filter(name=current_user_id).exists():
        reviewed = True

    if product_int in skus_list:
        purchased = True

    template = 'products/product_reviews.html'

    context = {
        'product': product,
        'product_review': product_review,
        'total_review': total_review,
        'avg_review': avg_review,
        'reviewed': reviewed,
        'purchased': purchased
    }

    return render(request, template, context)


@login_required
def add_review(request, slug):
    """
    A view to user review a product
    """
    if request.method == 'POST':
        review = request.POST.get('btnradio', None)
        user = request.user
        product = get_object_or_404(Product, slug=slug)

        if not review:
            messages.error(request, "You must select a rate score to review the product")
            return redirect("/")

        review_product_instance = ReviewProduct()
        review_product_instance.review = review
        review_product_instance.name = user
        review_product_instance.product = product
        review_product_instance.reviewed = True
        review_product_instance.save()

        messages.success(request, f'Successfully reviewed!')
        return redirect(request.META.get("HTTP_REFERER", "/"))
