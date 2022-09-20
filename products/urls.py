from django.urls import path
from . import views

urlpatterns = [
    path('all-products/', views.products, name='products')
]