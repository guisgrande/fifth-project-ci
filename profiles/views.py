from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.utils.safestring import mark_safe
from django.views import View
from django.utils import timezone
from checkout.models import Order
from management.models import Coupon
from .models import UserProfile
from .forms import UserProfileForm, UserDeleteForm


@login_required
def profile(request):
    """
    Function display the user's profile.
    POST update UserProfile model
    Display Coupon and update if expired
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    form = UserProfileForm(instance=profile)
    # Filter Coupon model by user and not used
    coupons = Coupon.objects.filter(user=request.user).filter(used=False)
    present = timezone.now()
    # Check if coupon is expired
    for coupon in coupons:
        if present >= coupon.date_end:
            coupon.expired = True
            coupon.save()
    # Filter Coupon model again including expired
    coupons = Coupon.objects.filter(user=request.user).filter(expired=False).filter(used=False)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
        'form': form,
        'coupons': coupons,
        'on_profile_page': True
    }

    return render(request, template, context)


@login_required
def delete_profile(request):
    """
    Function to delete profile/user, permanently.
    Loaded in other template.
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all()

    if request.method == 'POST':
        delete_form = UserDeleteForm(request.POST, instance=request.user)
        user = request.user
        user.delete()
        messages.info(request, 'Your account has been deleted.')
        return redirect('home')
    else:
        delete_form = UserDeleteForm(instance=request.user)

    context = {
        'delete_form': delete_form,
        'orders': orders
    }

    return render(request, 'profiles/delete_profile.html', context)


@login_required
def orders_list(request):
    """
    Function to display list of all orders for logged in user.
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all().order_by("-date")
    total_orders_list = orders.count()

    context = {
        'orders': orders,
        'total_orders_list': total_orders_list
    }

    return render(request, 'profiles/orders_list.html', context)


class OrderDetails(LoginRequiredMixin, View):
    """
    Class to display order details.
    Condition to verify if logged in user is the owner of the order.
    """
    
    def get(self, request, order_number, *args, **kwargs):
        queryset = Order.objects.all()
        order = get_object_or_404(queryset, order_number=order_number)
        if not request.user.is_superuser:
            if order.user_profile.user == self.request.user:
                return render(request, 'profiles/order_details.html', {
                    "order": order,
                })
            else:
                messages.error(request, mark_safe("""This order wasn't placed
                                        by you.<br/> Check order information
                                        again.<br/> My Account > My Profile >
                                        My Orders"""))
                return HttpResponseRedirect(reverse('home'))
        else:
            return render(request, 'profiles/order_details.html', {
                    "order": order,
                })

    def post(self, request, order_number, *args, **kwargs):
        queryset = Order.objects.all()
        order = get_object_or_404(queryset, order_number=order_number)
        if not request.user.is_superuser:
            if order.user_profile.user == self.request.user:
                return render(request, 'profiles/order_details.html', {
                    "order": order,
                })
            else:
                messages.error(request, mark_safe("""This order wasn't placed
                                        by you.<br/> Check order information
                                        again.<br/> My Account > My Profile >
                                        My Orders"""))
                return HttpResponseRedirect(reverse('home'))
        else:
            return render(request, 'profiles/order_details.html', {
                    "order": order,
                })
