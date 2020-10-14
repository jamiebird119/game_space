from django.urls import path
from . import views

urlpatterns = [
    path('bag/', views.get_bag, name="get_bag")
]
