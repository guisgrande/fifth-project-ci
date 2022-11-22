from django.urls import path
from . import views

urlpatterns = [
    path('all-products/', views.products, name='products'),
    path('details/<slug>/', views.product_details, name='product_details'),
    path('review-product/<slug>/', views.review_product,
         name='review_product'),
    path('add-review/<slug>/', views.add_review, name='add_review'),
]
