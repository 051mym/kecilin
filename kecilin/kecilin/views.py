from django.shortcuts import render
from mutation.models import Uang_masuk, Uang_keluar
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'dashboard/home.html', {
        
    })