from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=250)
    content = models.TextField()
    photo = models.ImageField(upload_to='photos/%y/%m/%d/')
    premiere = models.DateField(null=True, blank=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.name
