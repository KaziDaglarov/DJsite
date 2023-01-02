from django.db.models import Count
from .models import *

menu = [
    {'title':'О сайте', 'url_name':'about'},
    {'title':'Добавить фильм', 'url_name':'addMovies'},
    {'title':'Сериалы', 'url_name':'series'},
]

class DataMixin():
    paginate_by = 2
    def get_user_context(self, **kwargs):
        context = kwargs
        categories = Category.objects.annotate(Count('movie'))
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)
        context['menu'] = user_menu
        context['categories'] = categories
        if 'category_selected' not in context:
            context['category_selected'] = 0
        return context