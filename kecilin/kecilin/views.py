from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from .forms import UserForm

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
    
def user(request):
   
    data = User.objects.order_by('-id').all()
        
    datatable = create_page(request.GET.get('page'), data)
    
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user-list')
    else:
        form = UserForm()
    
    return render(request, 'pages/manage-data-user.html', {
        'datatable':datatable,
        'form':form,
    })
    

def user_delete(request, id):
    
    data = get_object_or_404(User, pk=id)
    data.delete()
        
    return redirect('user-list')

def user_form(request, id = None):
    
    if request.method == 'POST':
        if id:
            inst = get_object_or_404(User, pk=id)
            form = UserForm(request.POST, instance=inst)
        else:
            form = UserForm(request.POST)
        
        if form.is_valid():
            cleaned_data = form.cleaned_data

            id = cleaned_data.get('id', None)
            
            if not id:
                model = User()
                model.username = cleaned_data['username']
                model.email = cleaned_data['email']
                model.save()
            else:
                model = User.objects.get(pk=id)
                model.username = cleaned_data['username']
                model.email = cleaned_data['email']
                model.save()
            
            return redirect('user-list')
        else:
            print(form.errors)
    else:
        form = UserForm()
        
    return redirect('user-list')
     

