from django.urls import path
from . import views

urlpatterns = [
    path('all-products/', views.products, name='products'),
    path('details/<slug>/', views.product_details, name='product_details'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<slug>/', views.edit_product, name='edit_product'),
    path('delete/<slug>/', views.delete_product, name='delete_product'),
]
