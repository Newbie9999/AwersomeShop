"""awesome_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ProductListByCategory/', include('shop.urls', namespace='ProductListByCategory-shop')),
	url(r'^ProductDetail/', include('shop.urls', namespace='ProductDetail-shop')),
	url(r'^ProductList/', include('shop.urls', namespace='ProductList-shop')),
	url(r'^CartRemove/', include('cart.urls', namespace='CartRemove-cart')),
	url(r'^CartAdd/', include('cart.urls', namespace='CartAdd-cart')),
	url(r'^CartDetail/', include('cart.urls', namespace='CartDetail-cart')),
	url(r'^OrderCreate/', include('orders.urls', namespace='OrderCreate-orders')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 