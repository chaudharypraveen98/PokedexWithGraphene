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
        for pokemon_tag in pokemon["pokemon_tags"]:
            PokemonTag.objects.get_or_create(
                tag=pokemon_tag,
                pokemon=pokemon_obj
            )
        print(pokemon_obj.pokemon_id)
