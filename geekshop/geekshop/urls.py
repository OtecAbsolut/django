"""geekshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path

from mainapp import views as mainviews

urlpatterns = [
    path('', mainviews.main, name = 'main'),
    path('products/', mainviews.products, name = 'products'),
    path('products/all_product', mainviews.products, name = 'all_product'),
    path('products/home_product', mainviews.products, name = 'home_product'),
    path('products/modern_product', mainviews.products, name = 'modern_product'),
    path('products/office_product', mainviews.products, name = 'office_product'),
    path('products/classic_product', mainviews.products, name = 'classic_product'),
    path('contact/', mainviews.contact, name = 'contact'),
    path('admin/', admin.site.urls, name = 'admin'),
]

