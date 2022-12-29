from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404
from .models import Movie, Category

menu = [
    {'title':'О сайте', 'url_name':'about'},
    {'title':'Фильмы', 'url_name':'movies'},
    {'title':'Сериалы', 'url_name':'series'},
    {'title':'Войти', 'url_name':'login'},
]



def index(request):
    movies = Movie.objects.all()
    context = {
        'menu': menu,
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
    movie = get_object_or_404(Movie, pk=movie_id)
    context = {
        'movie': movie,
        'menu': menu,
        'title': movie.name,
        'category_selected': movie.category_id,
    }
    return render(request, 'cinema/movie.html', context=context)


def show_category(request, category_id):
    movies = Movie.objects.filter(category_id=category_id)
    if not len(movies):
        raise Http404()

    context = {
        'menu': menu,
        'movies': movies,
        'title': movies[0].category.name,
        'category_selected': category_id,
    }
    return render(request, 'cinema/index.html', context=context)