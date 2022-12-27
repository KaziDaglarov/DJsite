from django.urls import path
from .views import *



urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('movies/', movies, name='movies'),
    path('series/', series, name='series'),
    path('login/', login, name='login'),
    path('movie/<int:movie_id>/', show_movie, name='movie'),
    path('category/<int:category_id>/', show_category, name='category'),

]