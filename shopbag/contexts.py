from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product
from management.models import Coupon


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    coupon = request.session.get('code', None)
    bag = request.session.get('bag', {})

    for slug, quantity in bag.items():
        product = get_object_or_404(Product, slug=slug)
        if product.offer:
            total += quantity * (product.price - ((product.price * product.offer.offer_discount) / 100))
        else:
            total += quantity * product.price
        product_count += quantity
        bag_items.append ({
            'slug': slug,
            'quantity': quantity,
            'product': product,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    if not coupon:
        discount = 0
    else:
        get_coupon = get_object_or_404(Coupon, coupon=coupon)
        discount = get_coupon.discount

    total_discount = (delivery + total) * discount / 100
    grand_total = (delivery + total) - total_discount

    context = {
        'bag_items': bag_items,
        'coupon': coupon,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'discount': discount,
        'total_discount': total_discount,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
