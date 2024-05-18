from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
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

def home(request):
    data = User.objects.order_by('-id').all()
        
    datatable = create_page(request.GET.get('page'), data)
    
    return render(request, 'pages/manage-data-user.html', {
        'datatable':datatable
    })
    
def user(request):
   
    return render(request, 'pages/manage-data-user.html', {

    })
