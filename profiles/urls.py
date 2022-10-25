from django.urls import path
from . import views


urlpatterns = [
    path('user/', views.profile, name='profile'),
    path('delete-profile/', views.delete_profile, name='delete_profile'),
    path('my-orders/', views.orders_list, name='orders_list'),
    path('order/<order_number>', views.OrderDetails.as_view(), name='order_details'),
    path('orders-status/', views.orders_status, name='orders_status'),
    path('update-status/<str:pk>', views.update_status, name='update_status'),
]
