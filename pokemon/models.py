from django.db import models


class Pokemon(models.Model):
    pokemon_name = models.CharField(max_length=30)
    pokemon_url = models.CharField(max_length=30)
    pokemon_id = models.CharField(max_length=30, primary_key=True)
    pokemon_image_url = models.CharField(max_length=30)

    def __str__(self):
        return self.pokemon_id + self.pokemon_name


class PokemonTag(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    tag = models.CharField(max_length=20)

    def __str__(self):
        return self.tag
