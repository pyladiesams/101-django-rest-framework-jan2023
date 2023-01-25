from django.shortcuts import render
from rest_framework.views import APIView
from restaurants.models import Restaurants
from restaurants.serializer import RestaurantsSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework import generics, mixins


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
    
class RestaurantsListMixins(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Restaurants.objects.all()
    serializer_class = RestaurantsSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class RestaurantsDetailsMixins(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Restaurants.objects.all()
    serializer_class = RestaurantsSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)