"""streetcraft URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import handler400, handler403, handler404, handler500


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls'), name='home_urls'),
    path('', include('products.urls'), name='products_urls'),
    path('shop/', include('shopbag.urls'), name='shopbag_urls'),
    path('checkout/', include('checkout.urls'), name='checkout_urls'),
    path('profile/', include('profiles.urls'), name='profiles_urls'),
    path('management/', include('management.urls'), name='management_urls'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler400 = "streetcraft.views.handler400"
handler403 = 'streetcraft.views.handler403'
handler404 = "streetcraft.views.handler404"
handler500 = "streetcraft.views.handler500"
