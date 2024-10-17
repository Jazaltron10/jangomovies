from django.db import models
from users.models import User  # Importing the custom User model


# Movie model to store movie details
class Movie(models.Model):
    title = models.CharField(
        max_length=255, unique=True
    )  # Movie title should be unique
    release_date = models.DateField(
        null=True, blank=True
    )  # Optional field for the release date
    genre = models.CharField(
        max_length=100, null=True, blank=True
    )  # Optional field for the movie genre

    # String representation of the movie model (returns title)
    def __str__(self):
        return self.title


# Review model to store user reviews for movies
class Review(models.Model):
    movie = models.ForeignKey(
        Movie, related_name="reviews", on_delete=models.CASCADE
    )  # Link to Movie
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )  # Link to User (custom model)
    review_content = models.TextField()  # The content of the review
    rating = models.PositiveIntegerField()  # Rating out of 5
    created_date = models.DateTimeField(
        auto_now_add=True
    )  # Date the review was created

    # String representation of the review (returns movie title, rating, and user email)
    def __str__(self):
        return f"{self.movie.title} - {self.rating}/5 by {self.user.email}"
