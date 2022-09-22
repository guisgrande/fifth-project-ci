from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product, Category
from django.db.models import Q
from django.contrib import messages


def products(request):
    """
    A view to return the All products page,
    Search products funcionality, category return.
    """

    products_list = Product.objects.all()
    total_products_list = products_list.count()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products_list = products_list.filter(category__system_name__in=categories)
            categories = Category.objects.filter(system_name__in=categories)
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

    context = {
        "products_list": products_list,
        "total_products_list": total_products_list,
        'current_categories': categories,
    }

    return render(request, 'products_all.html', context)


def product_details(request, slug):
    """ A view to show individual product details and category """

    product = get_object_or_404(Product, slug=slug)

    context = {
        'product': product,
    }

    return render(request, 'product_details.html', context)
