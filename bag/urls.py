from django.urls import path
from . import views

urlpatterns = [
    path('bag/', views.get_bag, name="get_bag"),
    path('add/<game_id>/', views.add_to_bag, name="add_to_bag"),
    path('update/<game_id>/', views.adjust_bag, name='adjust_bag'),
    path('remove/<game_id>/', views.remove_item, name='remove_item')
]
