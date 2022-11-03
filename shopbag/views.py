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

    if product.quantity_available == 0:
        messages.error(request, f'Sorry! Out of stock.')
        return redirect(redirect_url)

    elif quantity > product.quantity_available:
        all_stock = product.quantity_available
        if slug in list(bag.keys()):
            bag[slug] += all_stock
            messages.success(request, f'Updated more {all_stock} for {product.name} quantity to {bag[slug]}')
        else:
            bag[slug] = all_stock
            messages.success(request, f'Added {all_stock} for {product.name} to your bag')     
        product.quantity_available = 0
        product.save()

    else:
        if slug in list(bag.keys()):
            bag[slug] += quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[slug]}')
        else:
            bag[slug] = quantity
            messages.success(request, f'Added {product.name} to your bag')
        product.quantity_available -= quantity
        product.save()

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
    old_quantity = bag[product.slug]

    if old_quantity > quantity:
        dif = old_quantity - quantity
        product.quantity_available += dif
        product.save()
        bag[slug] = quantity
        messages.success(request, f'Updated {product.name} quantity to {bag[slug]}')

    elif old_quantity < quantity:
        dif = quantity - old_quantity
        product.quantity_available -= dif
        product.save()
        bag[slug] = quantity
        messages.success(request, f'Updated {product.name} quantity to {bag[slug]}')

    elif quantity == 0: 
        bag.pop(slug)
        messages.success(request, f'Removed {product.name} from your bag')

    else:
        messages.info(request, 'No changes applied')

    request.session['bag'] = bag
    return redirect(reverse('bag'))


def remove_from_bag(request, slug):
    """
    Remove the product from the shopping bag
    """
    try:
        product = get_object_or_404(Product, slug=slug)
        bag = request.session.get('bag', {})
        old_quantity = bag[product.slug]
        product.quantity_available += old_quantity
        product.save()
        bag.pop(slug)
        messages.success(request, f'Removed {product.name} from your bag')
        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
