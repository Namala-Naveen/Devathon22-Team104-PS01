"""WSDC_admin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from basic_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('formpage/',views.formpage,name='formpage'),
    path('',views.loginpage,name='login'),
    path('register/',views.registrationpage,name='register'),
    path('admin_login/',views.adminlogin,name='adminlogin'),
    path('data/',views.adminlist,name='data'),
    path('payment/',views.payment,name='payment'),
]
