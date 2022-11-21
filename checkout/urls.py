from django.urls import path
from . import views
from .webhooks import webhook


urlpatterns = [
    path('order/', views.checkout, name='checkout'),
    path('order-success/<order_number>', views.checkout_success,
         name='checkout_success'),
    path('cache-checkout-data/', views.cache_checkout_data,
         name='cache_checkout_data'),
    path('wh/', webhook, name='webhook'),
]
