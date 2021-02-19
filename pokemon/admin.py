from django.contrib import admin

# Register your models here.
from pokemon.models import Pokemon, PokemonTag

admin.site.register(Pokemon)
admin.site.register(PokemonTag)
