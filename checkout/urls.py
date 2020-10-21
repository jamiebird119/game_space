from django.urls import path
from . import views


urlpatterns = [
    path('checkout/', views.checkout, name="checkout"),
    path('get_discount/', views.get_discount, name="get_discount")
]