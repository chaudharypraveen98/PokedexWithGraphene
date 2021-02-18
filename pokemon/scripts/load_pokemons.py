from PokedexWithGraphene import settings
from pokemon.models import Pokemon,PokemonTag
from pathlib import Path
import json
def run(*args):
    file_path = Path(settings.BASE_DIR, f'bill/old_bills/INV2020-21/INV{i:03d}.xlsm')
