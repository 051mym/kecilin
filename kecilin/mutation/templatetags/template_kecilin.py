from django import template

register = template.Library()

@register.filter(name='title_last_url')
def title_last_url(url):
    return url.split('/')[-1].replace('_', ' ').replace('-', ' ').title()