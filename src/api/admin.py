from django.contrib import admin
from .models import Movie
# Register your models here.

@admin.register(Movie)

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'rating', 'is_adult')   # columns shown in admin
    search_fields = ('title',)                               # adds a search box
    list_filter = ('year', 'is_adult')                       # adds filters in the sidebar