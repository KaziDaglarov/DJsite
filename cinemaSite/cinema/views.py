from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render
from .models import Movie, Category

menu = [
    {'title':'О сайте', 'url_name':'about'},
    {'title':'Фильмы', 'url_name':'movies'},
    {'title':'Сериалы', 'url_name':'series'},
    {'title':'Войти', 'url_name':'login'},
]



def index(request):
    movies = Movie.objects.all()
    categories = Category.objects.all()
    context = {
        'menu': menu,
        'categories':categories,
        'movies': movies,
        'title': 'glavnaya stranica',
        'category_selected': 0
    }
    return render(request, 'cinema/index.html', context=context)


def about(request):
    return render(request, 'cinema/about.html', {'menu': menu, 'title': 'o sayte'})

def pageNotFound(request, exceptions):
    return HttpResponseNotFound('<h1> Ne naydeno</h1>')

def movies(request):
    pass

def series(request):
    pass

def login(request):
    pass

def show_movie(request, movie_id):
    pass

def show_category(request, category_id):
    movies = Movie.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    if not len(movies):
        raise Http404()

    context = {
        'menu': menu,
        'categories': categories,
        'movies': movies,
        'title': f'{categories[category_id-1].name}',
        'category_selected': category_id,
    }
    return render(request, 'cinema/index.html', context=context)