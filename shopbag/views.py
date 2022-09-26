from django.shortcuts import render, redirect, reverse, HttpResponse


def view_bag(request):
    """
    A view to return the shopbag page
    """

    return render(request, 'shopbag/bag.html')


def add_to_bag(request, slug):
    """
    Add a quantity of the specified product to the shopping bag
    """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if slug in list(bag.keys()):
        bag[slug] += quantity
    else:
        bag[slug] = quantity

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)


def update_bag(request, slug):
    """
    Update the quantity of the product to the new amount
    """
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[slug] = quantity
    else:
        bag.pop(slug)

    request.session['bag'] = bag
    return redirect(reverse('bag'))


def remove_from_bag(request, slug):
    """
    Remove the product from the shopping bag
    """

    try:
        bag = request.session.get('bag', {})
        bag.pop(slug)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
