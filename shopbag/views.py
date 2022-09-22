from django.shortcuts import render


def shopbag(request):
    """ A view to return the shopbag page """

    return render(request, 'shopbag/bag.html')