from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100)
    genre = serializers.ListField(
        child = serializers.CharField(), allow_empty=False
    )
    year = serializers.IntegerField(min_value=1888)
    rating = serializers.DecimalField(
        max_digits=3, decimal_places=1, min_value=0.0, max_value=10.0
    )
    is_adult = serializers.BooleanField()

    class Meta:
        model = Movie
        fields = ["title", "genre", "year", "rating", "is_adult"]
    
    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Title cannot be blank")
        return value
    
    def validate_genre(self, value):
        if not all(isinstance(g, str) for g in value):
            raise serializers.ValidationError("Each genre must be string in a list")
        return value
    
    def validate_year(self, value):
        if value < 1888:
            raise serializers.ValidationError("year must be positive and greater than 1888")
        return value