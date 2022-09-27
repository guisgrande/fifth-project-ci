from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from products.models import Product
from django.contrib import messages


def view_bag(request):
    """
    A view to return the shopbag page
    """

    return render(request, 'shopbag/bag.html')


def add_to_bag(request, slug):
    """
    Add a quantity of the specified product to the shopping bag
    """
    product = get_object_or_404(Product, slug=slug)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if slug in list(bag.keys()):
        bag[slug] += quantity
        messages.success(request, f'Updated {product.name} quantity to {bag[slug]}')
    else:
        bag[slug] = quantity
        messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)


def update_bag(request, slug):
    """
    Update the quantity of the product to the new amount
    """
    product = get_object_or_404(Product, slug=slug)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[slug] = quantity
        messages.success(request, f'Updated {product.name} quantity to {bag[slug]}')
    else:
        bag.pop(slug)
        messages.success(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('bag'))


def remove_from_bag(request, slug):
    """
    Remove the product from the shopping bag
    """

    try:
        product = get_object_or_404(Product, slug=slug)
        bag = request.session.get('bag', {})
        bag.pop(slug)
        messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
