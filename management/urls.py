from django.urls import path
from . import views


urlpatterns = [
    path('news-letter-subscribe/', views.news_letter_sub, name='news_letter_sub'),
    path('news-letter-mails/', views.news_letter_view, name='news_letter_view'),
    path('news-letter-send/', views.news_letter_send, name='news_letter_send'),
    path('stock-control/', views.stock_control, name='stock_control'),
    path('update-stock/<slug>/', views.update_stock, name='update_stock'),
]
