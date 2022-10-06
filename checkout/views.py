from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    """
    Function to show checkout page.
    """
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag is empty at the moment.")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51LpsboL1ee1CsQAinhbqvK4fRfBSxM7mWqYYouhPQ1hAhp6i8OMTtltvCS7xxVIzeca7qP9fqKOH9m2QQeTQiR7d00RFaAHhus',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
