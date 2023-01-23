from django.db import models

class Restaurants(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=50)
    num_of_chefs = models.IntegerField(default=1)