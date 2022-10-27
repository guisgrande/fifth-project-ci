from django.urls import path
from . import views


urlpatterns = [
    path('news-letter-subscribe/', views.news_letter_sub, name='news_letter_sub'),
]