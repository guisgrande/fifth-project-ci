from django.shortcuts import render, get_object_or_404
from .models import Product


def products(request):
    """ A view to return the All products page """

    products_list = Product.objects.all()
    total_products_list = products_list.count()

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
