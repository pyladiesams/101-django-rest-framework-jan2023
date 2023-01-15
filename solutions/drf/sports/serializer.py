from rest_framework import serializers
from sports.models import Sports

class SportSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    num_of_players = serializers.IntegerField()
    sport_type = serializers.CharField()
    
    def create(self, validated_data):
        return Sports.objects.create(**validated_data)
    
    def update(self, instance, data):
        instance.name = data.get("name", instance.name)
        instance.description = data.get("description", instance.description)
        instance.num_of_players = data.get("num_of_players", instance.num_of_players)
        instance.sport_type = data.get("sport_type", instance.sport_type)
        
        instance.save()
        return instance