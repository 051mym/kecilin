from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Uang_masuk)
class UangMasukAdmin(admin.ModelAdmin):
    list_display = ["user_id", "datetime", "nominal"]
    fields = ('user_id', 'datetime', 'nominal')
    list_per_page = 10


@admin.register(Uang_keluar)
class UangMasukAdmin(admin.ModelAdmin):
    list_display = ["user_id", "datetime", "nominal"]
    fields = ('user_id', 'datetime', 'nominal')
    list_per_page = 10
