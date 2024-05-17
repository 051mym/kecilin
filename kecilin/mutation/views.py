from django.shortcuts import render, get_object_or_404, redirect
from mutation.models import Uang_masuk, Uang_keluar
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def uang_mutasi(request, type_mutation):
    
    if type_mutation == 'masuk':
        data = Uang_masuk.objects.all()
    elif type_mutation == 'keluar':
        data = Uang_keluar.objects.all()
    
    paginator  = Paginator(data, 10)
    
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
        'datatable': datatable,
        'type_mutation': type_mutation
    })


def uang_mutasi_delete(request, type_mutation, id):
    
    if type_mutation == 'masuk':
        data = get_object_or_404(Uang_masuk, pk=id)
        data.delete()
    elif type_mutation == 'keluar':
        data = get_object_or_404(Uang_keluar, pk=id)
        data.delete()
        
    return redirect('uang-mutasi', type_mutation=type_mutation)
    
    
