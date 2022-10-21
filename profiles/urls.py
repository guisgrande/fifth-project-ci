from django.urls import path
from . import views


urlpatterns = [
    path('user/', views.profile, name='profile'),
    path('delete-profile/', views.delete_profile, name='delete_profile'),
    path('my-orders/', views.orders_list, name='orders_list'),
    path('order/<order_number>', views.OrderDetails.as_view(), name='order_details'),
]
