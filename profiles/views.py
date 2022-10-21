from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm, UserDeleteForm


@login_required
def profile(request):
    """ 
    Function display the user's profile.
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    form = UserProfileForm(instance=profile)
   
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
        'form': form,
        'on_profile_page': True
    }

    return render(request, template, context)


@login_required
def delete_profile(request):
    """
    Function for delete profile/user, permanently.
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
    Function for display list of all order of the user.
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all()
    total_orders_list = orders.count()

    context = {
        'orders': orders,
        'total_orders_list': total_orders_list
    }

    return render(request, 'profiles/orders_list.html', context)
