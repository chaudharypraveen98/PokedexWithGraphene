import json
from pathlib import Path

from PokedexWithGraphene import settings
from pokemon.models import Pokemon, PokemonTag


def run(*args):
    file_path = Path(settings.BASE_DIR, 'pokemon/static/pokemon/pokemon.json')
    with open(file_path, encoding="utf8") as file:
        pokemon_data = json.loads(file.read())

    for pokemon in pokemon_data:
        pokemon_obj = Pokemon.objects.create(
            pokemon_url=pokemon["pokemon_url"],
            pokemon_name=pokemon["pokemon_name"],
            pokemon_id=pokemon["pokemon_id"],
            pokemon_image_url=pokemon["pokemon_image_url"]
        )
        pokemon_obj.pokemon_tag.add(*list(PokemonTag.objects.get_or_create(tag=pokemon)[0].id for pokemon in pokemon['pokemon_tags']))
        print(pokemon_obj.pokemon_id)
