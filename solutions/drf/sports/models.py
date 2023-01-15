from django.db import models

# Create your models here.

class Sports(models.Model):
    
    SPORT_TYPE_CHOICES = (
        ("Indoor", "indoor"),
        ("Outdoor", "outdoor"),)
    
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    num_of_players = models.IntegerField()
    sport_type = models.CharField(max_length=10, choices=SPORT_TYPE_CHOICES)
    
    def __str__(self) -> str:
        return self.name