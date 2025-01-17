from django.db import models
from django.utils import timezone

class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    about = models.TextField(blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    movie_image = models.ImageField(null=True, blank=True, upload_to='images/')