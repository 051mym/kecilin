"""
URL configuration for kecilin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.urls import path, include
from mutation import views
from django.conf.urls.static import static

urlpatterns = [
    path('uang-<slug:type_mutation>', views.uang_mutasi, name='uang-mutasi'),
    path('uang-<slug:type_mutation>/delete/<int:id>', views.uang_mutasi_delete, name='uang-mutasi-delete'),
    path('uang-<slug:type_mutation>/form', views.uang_mutasi_form, name='uang-mutasi-form'),
    # path('uang-<slug:type_mutation>/form/<int:id>', views.uang_mutasi_form, name='uang-mutasi-from'),
    
]
