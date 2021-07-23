from django.urls import path

from pokemon import views

app = 'pokemom'

urlpatterns = [
    path('',views.pokemon_home),
]