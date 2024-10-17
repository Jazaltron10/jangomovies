from django.contrib import admin
from .models import Review, Movie

admin.site.register(Review)  # Register the Review model
admin.site.register(Movie)  # Register the Movie model
