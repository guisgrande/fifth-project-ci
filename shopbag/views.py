from django.shortcuts import render, redirect


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
