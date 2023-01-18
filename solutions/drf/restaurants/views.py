from django.shortcuts import render
from rest_framework.views import APIView
from restaurants.models import Restaurants
from restaurants.serializer import RestaurantsSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


class RestaurantsList(APIView):
    def get(self, request):
        restaurants = Restaurants.objects.all()
        serializer = RestaurantsSerializer(restaurants, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = RestaurantsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

class RestaurantsDetail(APIView):
    def get_restaurant(self, pk):
        try:
            return Restaurants.objects.get(pk=pk)
        except Restaurants.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        restaurant = self.get_restaurant(pk)
        serializer = RestaurantsSerializer(restaurant)
        return Response(serializer.data)
    
    def put(self, request, pk):
        restaurant = self.get_restaurant(pk)
        serializer = RestaurantsSerializer(restaurant, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        restaurant = self.get_restaurant(pk)
        restaurant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)