from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from sports.models import Sports
from sports.serializer import SportSerializer

@api_view(["GET", "POST"])
def sports_list(request):
    if request.method == "GET":
        sports = Sports.objects.all()
        serializer = SportSerializer(sports, many=True)
        return Response(serializer.data)
    
    if request.method == "POST":
        serializer = SportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(["GET", "PUT", "DELETE"])
def sports_detail(request, pk):
    try:
        sport = Sports.objects.get(pk=pk)
    except Sports.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = SportSerializer(sport)
        return Response(serializer.data)
    
    if request.method == "PUT":
        serializer = SportSerializer(sport, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == "DELETE":
        sport.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)