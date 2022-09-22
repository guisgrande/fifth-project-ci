from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product
from django.db.models import Q
from django.contrib import messages


def products(request):
    """
    A view to return the All products page,
    Search products funcionality
    """

    products_list = Product.objects.all()
    total_products_list = products_list.count()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products_list = products_list.filter(queries)

    context = {
        "products_list": products_list,
        "total_products_list": total_products_list,
    }

    return render(request, 'products_all.html', context)


def product_details(request, slug):
    """ A view to show individual product details and category """

    product = get_object_or_404(Product, slug=slug)

    context = {
        'product': product,
    }

    return render(request, 'product_details.html', context)
