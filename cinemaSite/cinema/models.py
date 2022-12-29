from django.db import models
from django.urls import reverse


class Movie(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField()
    photo = models.ImageField(upload_to='photos/%y/%m/%d/', null=True)
    premiere = models.DateField(null=True, blank=True)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('movie', kwargs={'movie_slug': self.slug})

    class Meta:
        verbose_name = 'Фильмы'
        verbose_name_plural = 'Фильмы'
        ordering = ['name']

class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})
    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'
        ordering = ['name']