from django.shortcuts import render
from mutation.models import Uang_masuk, Uang_keluar
from django.http import HttpResponse
from django.apps import apps
from django.conf import settings
# Create your views here.


def home(request):
    all_apps = apps.get_app_configs()
    user_apps = [ apps for apps in all_apps if apps.name in settings.USER_APPS ]
    
    for app in user_apps:
        print(app.name, ":")
        for model in app.get_models():
            print("\t", model)
    return render(request, 'pages/manage-data.html', {

    })
