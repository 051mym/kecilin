from django.shortcuts import render, get_object_or_404, redirect
from mutation.models import Uang_masuk, Uang_keluar
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import UangMutationForm
from .serializers import MutasiSerializer

# Create your views here.

def create_page(page, data):
    paginator  = Paginator(data, 10)
    
    try:
        datatable = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        datatable = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver last page of results.
        datatable = paginator.page(paginator.num_pages)
    
    return datatable
    

def uang_mutasi(request, type_mutation):
    
    if type_mutation == 'masuk':
        data = Uang_masuk.objects.order_by('-datetime').all()
    elif type_mutation == 'keluar':
        data = Uang_keluar.objects.order_by('-datetime').all()
        
    datatable = create_page(request.GET.get('page'), data)
    
    if request.method == 'POST':
        form = UangMutationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('uang-mutasi', type_mutation=type_mutation)
    else:
        form = UangMutationForm()


    return render(request, 'pages/manage-data-mutasi.html', {
        'datatable': datatable,
        'type_mutation': type_mutation,
        'form' : form,
        'serializer': MutasiSerializer,
    })


def uang_mutasi_delete(request, type_mutation, id):
    
    if type_mutation == 'masuk':
        data = get_object_or_404(Uang_masuk, pk=id)
        data.delete()
    elif type_mutation == 'keluar':
        data = get_object_or_404(Uang_keluar, pk=id)
        data.delete()
        
    return redirect('uang-mutasi', type_mutation=type_mutation)

def uang_mutasi_form(request, type_mutation, id = None):
    
    if request.method == 'POST':
        form = UangMutationForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data

            id = cleaned_data.get('id', None)
            
            if not id:
                model = Uang_keluar() if type_mutation == 'keluar' else Uang_masuk()
                model.user_id = cleaned_data['user_id']
                model.nominal = cleaned_data['nominal']
                model.datetime = cleaned_data['datetime']
                model.save()
            else:
                model = Uang_keluar.objects.get(pk=id) if type_mutation == 'keluar' else Uang_masuk.objects.get(pk=id)
                model.user_id = cleaned_data['user_id']
                model.nominal = cleaned_data['nominal']
                model.datetime = cleaned_data['datetime']
                model.save()
            
            return redirect('uang-mutasi', type_mutation=type_mutation)
    else:
        form = UangMutationForm()
        
    return redirect('uang-mutasi', type_mutation=type_mutation)
     

    
    
