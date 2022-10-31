from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Avg
from django.contrib import messages
from .models import Product, Category, Offer, ReviewProduct
from .forms import ProductForm


def products(request):
    """
    A view to return the All products page,
    Search and sort products funcionality, 
    Category return from nav links.
    """

    products_list = Product.objects.all()
    total_products_list = products_list.count()
    query = None
    categories = None
    offers = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
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

    current_sorting = f'{sort}_{direction}'

    context = {
        "products_list": products_list,
        "total_products_list": total_products_list,
        'current_categories': categories,
        'current_sorting': current_sorting
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
def add_product(request):
    """
    A view to admin add new products to store database
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_details', args=[product.slug]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, slug):
    """
    A view to admin edit products from store database
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, slug=slug)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully updated {product.name}!')
            return redirect(reverse('product_details', args=[product.slug]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, slug):
    """
    A view to admin delete products from store database
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, slug=slug)
    product.delete()
    messages.success(request, 'Product deleted!')

    return redirect(reverse('products'))


@login_required
def review_product(request, slug):
    """
    A view to user review a product
    """

    product = get_object_or_404(Product, slug=slug)
    product_review = product.product_review.filter(reviewed=True).order_by("-created_on")
    total_review = product_review.count()
    avg_review = product.product_review.aggregate(review=Avg('review'))['review']

    template = 'products/product_reviews.html'

    context = {
        'product': product,
        'product_review': product_review,
        'total_review': total_review,
        'avg_review': avg_review
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
