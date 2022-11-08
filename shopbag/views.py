from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from products.models import Product
from management.models import Coupon
from django.contrib import messages
from django.utils import timezone


def view_bag(request):
    """
    A view to return the shopbag page
    And verify coupon
    """
    coupon = None
    valid_coupon = False

    if request.method == 'POST':
        if request.user.is_authenticated:
            coupons = Coupon.objects.filter(user=request.user).filter(used=False)
            present = timezone.now()
            # Check if coupon is expired
            for coupon in coupons:
                if present >= coupon.date_end:
                    coupon.expired = True
                    coupon.save()
            # Filter Coupon model again including expired
            coupons = Coupon.objects.filter(user=request.user).filter(expired=False).filter(used=False)
            coupon = request.POST.get('coupon', None)

            if str(coupon) == str(coupons[0]):
                messages.success(request, 'Coupon applied successfully')
                valid_coupon = True
            else:
                messages.error(request, 'Something is wrong. This coupon is not valid')

    template = 'shopbag/bag.html'
    context = {
        'coupon': coupon,
        'valid_coupon': valid_coupon,
    }

    return render(request, template, context)


def add_to_bag(request, slug):
    """
    Add a quantity of the specified product to the shopping bag
    """
    product = get_object_or_404(Product, slug=slug)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    current_quantity = 0

    # When no stock
    if product.quantity_available == 0:
        messages.error(request, f'Sorry! Out of stock.')
        return redirect(redirect_url)

    # Get quantity from bag if have the product
    if slug in list(bag.keys()):
        current_quantity = bag[product.slug]
    else:
        current_quantity = 0
    
    # Conditions to verify quantity in bag vs available stock
    if current_quantity < product.quantity_available:
        if quantity >= product.quantity_available:
            all_stock = product.quantity_available
            if slug in list(bag.keys()):
                bag[slug] = all_stock
                messages.success(request, f'Updated to {all_stock} (Maximum available stock) for {product.name} quantity to {bag[slug]}')
            else:
                bag[slug] = all_stock
                messages.success(request, f'Added {all_stock} (Maximum available stock) for {product.name} to your bag')
        else:
            if slug in list(bag.keys()):
                sum = current_quantity + quantity
                if sum < product.quantity_available:
                    bag[slug] += quantity
                    messages.success(request, f'Updated {product.name} quantity to {bag[slug]}')
                else:
                    all_stock = product.quantity_available
                    bag[slug] = all_stock
                    messages.success(request, f'Updated to {all_stock} (Maximum available stock) for {product.name}')
            else:
                bag[slug] = quantity
                messages.success(request, f'Added {product.name} to your bag')
    else: 
        all_stock = product.quantity_available
        bag[slug] = all_stock
        messages.success(request, f'{all_stock} (Maximum available stock) for {product.name} at your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def update_bag(request, slug):
    """
    Update the quantity of the product to the new amount
    """
    product = get_object_or_404(Product, slug=slug)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity == 0: 
        bag.pop(slug)
        messages.success(request, f'Removed {product.name} from your bag')
    
    if quantity <= product.quantity_available:
        bag[slug] = quantity
        messages.success(request, f'Updated {product.name} quantity to {bag[slug]}')

    elif quantity > product.quantity_available:
        all_stock = product.quantity_available
        bag[slug] = all_stock
        messages.success(request, f'Updated {product.name} quantity to {bag[slug]} (Maximum available stock)')

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
        bag.pop(slug)
        messages.success(request, f'Removed {product.name} from your bag')
        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
