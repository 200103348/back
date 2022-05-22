from django import template
from myapp.models import *
register=template.Library()

@register.simple_tag(name="getcats")
def get_categories():
    return Tokyo.objects.all()

@register.inclusion_tag('myapp/banner.html')
def show_categories():
    tag = Tag.objects.all()
    return {'tag': tag}