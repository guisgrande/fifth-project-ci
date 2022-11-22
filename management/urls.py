from django.urls import path
from . import views


urlpatterns = [
    path('add-product/', views.add_product, name='add_product'),
    path('edit-product/<slug>/', views.edit_product, name='edit_product'),
    path('delete-product/<slug>/', views.delete_product,
         name='delete_product'),
    path('news-letter-subscribe/', views.news_letter_sub,
         name='news_letter_sub'),
    path('news-letter-mails/', views.news_letter_view,
         name='news_letter_view'),
    path('news-letter-send/', views.news_letter_send, name='news_letter_send'),
    path('stock-control/', views.stock_control, name='stock_control'),
    path('update-stock/<slug>/', views.update_stock, name='update_stock'),
    path('orders-status/', views.orders_status, name='orders_status'),
    path('update-status/<str:pk>', views.update_status, name='update_status'),
]
