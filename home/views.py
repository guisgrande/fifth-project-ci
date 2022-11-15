from django.shortcuts import render
from products.models import Product


def index(request):
    """
    A view to return the index page
    """

    # List for Special Sale (Offer SKU 2)
    special_list = Product.objects.filter(offer=2).order_by("-release_date")[0:4]
    # List for New Arrivals (Offer SKU 1)
    news_list = Product.objects.filter(offer=1).order_by("-release_date")[0:4]
    # List for Last Oportinity (Offer SKU 2)
    last_list = Product.objects.filter(offer=3).order_by("-release_date")[0:4]

    context = {
        "special_list": special_list,
        "news_list": news_list,
        "last_list": last_list,
    }

    return render(request, 'index.html', context)
