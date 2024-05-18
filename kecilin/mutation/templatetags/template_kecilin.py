from django import template
import json
register = template.Library()
from mutation.serializers import MutasiSerializer
from kecilin.serializers import UserSerializer

@register.filter(name='title_last_url')
def title_last_url(url):
    return url.split('/')[-1].replace('_', ' ').replace('-', ' ').title()

@register.filter(name='serizmutasi')
def serizmutasi(object):
    data = MutasiSerializer(object)
    return data.data

@register.filter(name='serizuser')
def serizuser(object):
    data = UserSerializer(object)
    return data.data