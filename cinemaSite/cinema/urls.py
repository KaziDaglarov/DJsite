from django.urls import path
from .views import *



urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('addmovies/', addMovies, name='addMovies'),
    path('series/', series, name='series'),
    path('login/', login, name='login'),
    path('movie/<slug:movie_slug>/', show_movie, name='movie'),
    path('category/<slug:category_slug>/', show_category, name='category'),

]