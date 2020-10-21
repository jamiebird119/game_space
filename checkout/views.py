from django.shortcuts import render, redirect
from .forms import OrderForm
from django.contrib import messages
from .models import Discount

# Create your views here.


def checkout(request):
    order_form = OrderForm
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form
    }
    return render(request, template, context)


def get_discount(request):
    discount_code = request.POST.get('discount-code')
    discount = Discount.objects.all()
    redirect_url = request.POST.get('redirect_url')
    for thing in discount:
        if thing.code == discount_code:
            request.session['discount'] = discount_code
            messages.success(request, f'Successfully applied discount code: {discount_code}')
        else:
            messages.error(request, f'Could not find discount_code: {discount_code}. Please check spelling and try again.')
    return redirect(redirect_url)

