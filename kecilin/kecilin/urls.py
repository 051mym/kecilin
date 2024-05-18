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
from .views import user, user_delete, user_form
from django.conf.urls.static import static

urlpatterns = [
    path('', user, name='home'),
    path('user', user, name='user-list'),
    path('user/delete/<int:id>', user_delete, name='user-delete'),
    path('user/form', user_form, name='user-form'),
    path('user/form/<int:id>', user_form, name='user-form-id'),

    
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('mutation/', include('mutation.urls')),
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
