from django.urls import path
from .views import *



urlpatterns = [
    path('', MovieHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addmovies/', AddMovie.as_view(), name='addMovies'),
    path('series/', series, name='series'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('movie/<slug:movie_slug>/', MovieShow.as_view(), name='movie'),
    path('category/<slug:category_slug>/', MovieCategory.as_view(), name='category'),

]