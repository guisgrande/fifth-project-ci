from django.urls import path
from . import views

urlpatterns = [
    path('bag/', views.view_bag, name='bag'),
    path('add/<slug>/', views.add_to_bag, name='add_to_bag'),
    path('update/<slug>/', views.update_bag, name='update_bag'),
    path('remove/<slug>/', views.remove_from_bag, name='remove_from_bag'),
]
