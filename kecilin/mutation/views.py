from django.shortcuts import render
from mutation.models import Uang_masuk, Uang_keluar
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def uang_masuk(request):
    uang_masuk = Uang_masuk.objects.all()
    paginator  = Paginator(uang_masuk, 10)
    
    page = request.GET.get('page')
    try:
        datatable = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        page = 1
        datatable = paginator.page(page)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver last page of results.
        page = paginator.num_pages
        datatable = paginator.page(page)


    return render(request, 'pages/manage-data.html', {
        'uang_masuk': uang_masuk,
        'datatable': datatable
    })


def uang_keluar(request):
    uang_keluar = Uang_keluar.objects.all()
    page = Paginator(uang_keluar, 10)
    
    return render(request, 'pages/manage-data.html', {
        'uang_keluar': uang_keluar,
        'page': page
    })
