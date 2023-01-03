from django.db.models import Count
from .models import *
from django.core.cache import cache

menu = [
    {'title':'О сайте', 'url_name':'about'},
    {'title':'Добавить фильм', 'url_name':'addMovies'},
    {'title':'Обратная связь', 'url_name':'contact'},
]

class DataMixin():
    paginate_by = 2
    def get_user_context(self, **kwargs):
        context = kwargs
        categories = cache.get('categories')
        if not categories:
            categories = Category.objects.annotate(Count('movie'))
            cache.set('categories', categories, 60)

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)

        context['menu'] = user_menu

        context['categories'] = categories
        if 'category_selected' not in context:
            context['category_selected'] = 0
        return context