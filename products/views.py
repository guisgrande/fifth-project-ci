from django.shortcuts import render
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
