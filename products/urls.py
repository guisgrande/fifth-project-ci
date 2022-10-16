from django.urls import path
from . import views

urlpatterns = [
    path('all-products/', views.products, name='products'),
    path('details/<slug>/', views.product_details, name='product_details'),
    path('add/', views.add_product, name='add_product'),
]
