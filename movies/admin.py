from django.contrib import admin
from .models import Genre, Movie

class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'genre')

admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)