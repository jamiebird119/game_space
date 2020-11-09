from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required
import datetime
import json
import base64
import requests
import hashlib

# Create your views here.


@login_required
def profile(request):
    template = 'profiles/profile.html'
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Successfully updated delivery information.')
        else:
            messages.error(
                request, 'Failed to update/add user information. Please ensure form is valid')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    context = {
        'profile': profile,
        'orders': orders,
        'form': form,
    }
    return render(request, template, context)


def add_profile_photo(request):
    template = 'profiles/profile.html'
    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all()
    if request.method == 'POST':
        image_file = request.FILES["user_image"]
        profile.user_image = image_file
        profile.save()
        messages.success(
            request, 'Successfully updated profile image information.')
    else:
        print("not post request")
        messages.error(
            request, 'Failed to upload profile image. Please try again')
    context = {
        'profile': profile,
        'orders': orders,
        'form': UserProfileForm(instance=profile),
    }
    return render(request, template, context)


@login_required
def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    messages.info(request,
                  (f'This is a past order confirmation for order number {order_number}.'
                   'A confirmation email was sent on the order date'
                   ))
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }
    return render(request, template, context)

