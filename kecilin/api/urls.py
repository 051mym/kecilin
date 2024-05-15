
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('mutation-list', MutationList.as_view(), name='mutation-list'),
]
