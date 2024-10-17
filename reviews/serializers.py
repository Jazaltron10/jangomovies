from rest_framework import serializers
from .models import Movie, Review
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username']

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'release_date', 'genre']

class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)
    movie_id = serializers.PrimaryKeyRelatedField(
        queryset=Movie.objects.all(), 
        write_only=True,
        source='movie'
    )
    user = serializers.StringRelatedField(read_only=True)
    user_details = UserSerializer(source='user', read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'movie', 'movie_id', 'user', 'user_details', 'review_content', 'rating', 'created_date']
        read_only_fields = ['user', 'user_details', 'created_date']

    def validate_rating(self, value):
        if not 1 <= value <= 5:
            raise serializers.ValidationError("Rating must be between 1 and 5.")
        return value

class MovieDetailSerializer(MovieSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta(MovieSerializer.Meta):
        fields = MovieSerializer.Meta.fields + ['reviews']
