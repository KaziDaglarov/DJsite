from django.contrib import admin
from .models import *

class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'photo', 'is_published')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published',)
    prepopulated_fields = {'slug': ('name',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Movie, MovieAdmin)
admin.site.register(Category, CategoryAdmin)