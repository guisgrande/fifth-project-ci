from django.urls import path
from . import views
from .webhooks import webhook


urlpatterns = [
    path('order/', views.checkout, name='checkout'),
    path('order_success/<order_number>', views.checkout_success, name='checkout_success'),
    path('wh/', webhook, name='webhook'),
]
