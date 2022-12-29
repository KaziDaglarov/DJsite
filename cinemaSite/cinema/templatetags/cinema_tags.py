from django import template
from cinema.models import *

register = template.Library()

@register.simple_tag()
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(id=filter)

@register.inclusion_tag('cinema/list_categories.html')
def show_categories(sort=None, category_selected=None):
    if not sort:
        categories = Category.objects.all()
    else:
        categories = Category.objects.order_by(sort)
    return {'categories': categories, 'category_selected': category_selected}
