from django.contrib import admin
from django.urls import path
from sports.views import sports_list, sports_detail

urlpatterns = [
    path('list/', sports_list),
    path('detail/<int:pk>', sports_detail)
]