from django.contrib import admin
from django.urls import path
from restaurants.views import RestaurantsList, RestaurantsDetail

urlpatterns = [
    path('list/', RestaurantsList.as_view()),
    path('detail/<int:pk>', RestaurantsDetail.as_view()),
]