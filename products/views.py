from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product, Category, Offer
from django.db.models import Q
from django.contrib import messages
from django.db.models.functions import Lower


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
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products_all.html', context)


def product_details(request, slug):
    """ A view to show individual product details and category """

    product = get_object_or_404(Product, slug=slug)

    context = {
        'product': product,
    }

    return render(request, 'products/product_details.html', context)
