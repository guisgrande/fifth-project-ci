from django.urls import path
from . import views

urlpatterns = [
    path('all-products/', views.products, name='products'),
    path('<slug>/', views.product_details, name='product_details')
]
