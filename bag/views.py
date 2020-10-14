from django.shortcuts import render

# Create your views here.


def get_bag(request):
    template = 'bag/bag.html'
    context = {

    }
    return render(request, template, context)
