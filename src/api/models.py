from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.
# Db level validation

class Movie(models.Model):
    title = models.CharField(max_length=200)
    genre = models.JSONField(default=list)
    year = models.PositiveIntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    is_adult = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} - {self.year}"
    
    def clean(self):
        if not self.title.strip():
            raise ValidationError("title cannot be blank!")
            
        if not isinstance(self.genre, list):
            raise ValidationError("genre must be a list ")
        
        if not self.year:
            raise ValidationError("year must be positive integer")
        
        if not (0.0 < self.rating <= 10.0):
            raise ValidationError("ratings must be in range 0-10")
    
    def save(self, *args, **kwargs):
        self.full_clean()  # Automatically runs clean() + field validations
        super().save(*args, **kwargs)