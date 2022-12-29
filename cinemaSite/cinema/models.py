from django.db import models
from django.urls import reverse


class Movie(models.Model):
    name = models.CharField(max_length=250)
    content = models.TextField()
    photo = models.ImageField(upload_to='photos/%y/%m/%d/')
    premiere = models.DateField(null=True, blank=True)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('movie', kwargs={'movie_id': self.pk})

    class Meta:
        verbose_name = 'Фильмы'
        verbose_name_plural = 'Фильмы'
        ordering = ['name']

class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})
    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'
        ordering = ['name']