from django.urls import path
from . import views

urlpatterns = [
    path('bag/', views.view_bag, name='bag')
]
