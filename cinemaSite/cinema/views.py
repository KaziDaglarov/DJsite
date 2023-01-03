from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from .models import Movie, Category
from django.views.generic import ListView, DetailView, CreateView, FormView
from .forms import *
from .utils import *
from django.contrib.auth.mixins import  LoginRequiredMixin




class MovieHome(DataMixin, ListView):
    model = Movie
    template_name = 'cinema/index.html'
    context_object_name = 'movies'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))
    def get_queryset(self):
        return Movie.objects.filter(is_published=True).select_related('category')


def about(request):
    return render(request, 'cinema/about.html', {'menu': menu, 'title': 'o sayte'})

def pageNotFound(request, exceptions):
    return HttpResponseNotFound('<h1> Ne naydeno</h1>')

class AddMovie(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddMovieForm
    template_name = 'cinema/addmovie.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление страницы')
        return dict(list(context.items()) + list(c_def.items()))




class ContactFormView(FormView, DataMixin):
    template_name = 'cinema/contact.html'
    success_url = reverse_lazy('home')
    form_class = ContactForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Обратная связь')
        return dict(list(context.items()) + list(c_def.items()))


    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')



class MovieShow(DataMixin, DetailView):
    model = Movie
    template_name = 'cinema/movie.html'
    slug_url_kwarg = 'movie_slug'
    context_object_name = 'movie'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['movie'])
        return dict(list(context.items()) + list(c_def.items()))



class MovieCategory(DataMixin, ListView):
    model = Category
    template_name = 'cinema/index.html'
    context_object_name = 'movies'


    def get_queryset(self):
        return Movie.objects.filter(category__slug=self.kwargs['category_slug'], is_published=True).select_related('category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Category.objects.get(slug=self.kwargs['category_slug'])
        c_def = self.get_user_context(title='Категория - ' + str(c.name),
                                      category_selected=c.pk)
        return dict(list(context.items()) + list(c_def.items()))

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'cinema/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'cinema/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('login')