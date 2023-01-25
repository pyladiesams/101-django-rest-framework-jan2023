from django.contrib import admin
from django.urls import path
from restaurants.views import RestaurantsList, RestaurantsDetail, RestaurantsListMixins, RestaurantsDetailsMixins

urlpatterns = [
    path('list/', RestaurantsList.as_view()),
    path('detail/<int:pk>', RestaurantsDetail.as_view()),
    path('list-mixins/', RestaurantsListMixins.as_view()),
    path('detail-mixins/<int:pk>', RestaurantsDetailsMixins.as_view())
]