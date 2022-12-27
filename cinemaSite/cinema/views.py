from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .models import Movie

menu = [
    {'title':'О сайте', 'url_name':'about'},
    {'title':'Фильмы', 'url_name':'movies'},
    {'title':'Сериалы', 'url_name':'series'},
    {'title':'Войти', 'url_name':'login'},
]



def index(request):
    movies = Movie.objects.all()
    return render(request, 'cinema/index.html', {'menu': menu, 'movies': movies, 'title': 'glavnaya stranica'})


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