from django.shortcuts import render

def products(request):
    """ A view to return the All products page """

    return render(request, 'products_all.html')
