from django.urls import path
from .views import *



urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('movies/', movies, name='movies'),
    path('series/', series, name='series'),
    path('login/', login, name='login'),

]