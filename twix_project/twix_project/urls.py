"""
URL configuration for twix_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
import twixapp1.views
from twixapp1.views import start_page, show_product1, product1
from twixapp2.views import show_product2, product2

urlpatterns = [
    path('', start_page),
    path('product1/', product1, name='product1'),
    path('product2/', product2, name='product2'),
    path('<int:product1_id>/', show_product1),
    path('<int:product2_id>/', show_product2),
    path('admin/', admin.site.urls),
]
