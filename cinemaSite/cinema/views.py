from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Category
from django.views.generic import ListView
from .forms import *

menu = [
    {'title':'О сайте', 'url_name':'about'},
    {'title':'Добавить фильм', 'url_name':'addMovies'},
    {'title':'Сериалы', 'url_name':'series'},
    {'title':'Войти', 'url_name':'login'},
]


class MovieHome(ListView):
    model = Movie

# def index(request):
#     movies = Movie.objects.all()
#     context = {
#         'menu': menu,
#         'movies': movies,
#         'title': 'glavnaya stranica',
#         'category_selected': 0
#     }
#     return render(request, 'cinema/index.html', context=context)


def about(request):
    return render(request, 'cinema/about.html', {'menu': menu, 'title': 'o sayte'})

def pageNotFound(request, exceptions):
    return HttpResponseNotFound('<h1> Ne naydeno</h1>')

def addMovies(request):
    if request.method=='POST':
        form = AddMovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = AddMovieForm()
    return render(request, 'cinema/addmovie.html', {'form': form, 'menu': menu, 'title': 'Добавление статьи'})

def series(request):
    pass

def login(request):
    pass

def show_movie(request, movie_slug):
    movie = get_object_or_404(Movie, slug=movie_slug)
    context = {
        'movie': movie,
        'menu': menu,
        'title': movie.name,
        'category_selected': movie.category.slug,
    }
    return render(request, 'cinema/movie.html', context=context)


def show_category(request, category_slug):
    movies = Movie.objects.filter(category__slug=category_slug)
    if not len(movies):
        raise Http404()

    context = {
        'menu': menu,
        'movies': movies,
        'title': movies[0].category.name,
        'category_selected': category_slug,
    }
    return render(request, 'cinema/index.html', context=context)