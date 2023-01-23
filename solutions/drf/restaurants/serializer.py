from rest_framework import serializers
from rest_framework.serializers import ValidationError
from restaurants.models import Restaurants

class RestaurantsSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()
    
    class Meta:
        model = Restaurants
        fields = "__all__"
        
    def validate_num_of_chefs(self, data):
        if data < 1:
            raise ValidationError("Number of chefs cannot be less than 1.")
        return data
        
    def get_description(self, obj):
        return f"Restaurant {obj.name} is located in {obj.city}."