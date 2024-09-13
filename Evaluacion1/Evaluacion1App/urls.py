from django.contrib import admin
from django.urls import path, include

from Evaluacion1App import views

urlpatterns = [
    path('Peliculas/', views.Peliculas),
    path('Peliculas/Batman1/', views.Batman1),
    path('Peliculas/Batman2/', views.Batman2),
    path('Peliculas/Batman3/', views.Batman3),
]