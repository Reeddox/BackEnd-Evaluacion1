from django.contrib import admin
from django.urls import path, include

from Evaluacion1App import views

urlpatterns = [
    path('Armas/', views.Armas),
    path('Espada/', views.Espada),
    path('Escudo/', views.Escudo),
    path('Arco/', views.Arco),
]