from django.shortcuts import render


def view_bag(request):
    """ A view to return the shopbag page """

    return render(request, 'shopbag/bag.html')
