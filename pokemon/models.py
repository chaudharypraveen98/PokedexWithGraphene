from django.db import models


class PokemonTag(models.Model):
    tag = models.CharField(max_length=20)

    def __str__(self):
        return self.tag


class Pokemon(models.Model):
    pokemon_name = models.CharField(max_length=30)
    pokemon_url = models.CharField(max_length=30)
    pokemon_id = models.CharField(max_length=30, primary_key=True)
    pokemon_image_url = models.CharField(max_length=30)
    pokemon_tag = models.ManyToManyField(PokemonTag, related_name='pokemon')

    def __str__(self):
        return f"{self.pokemon_id}  {self.pokemon_name}"
