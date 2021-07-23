import graphene
from graphene_django.types import DjangoObjectType

from .models import Pokemon, PokemonTag


class PokemonType(DjangoObjectType):
    class Meta:
        model = Pokemon
        field = '__all__'


class PokemonTagType(DjangoObjectType):
    class Meta:
        model = PokemonTag


class Query(graphene.ObjectType):
    all_pokemons = graphene.List(PokemonType)
    pokemon_by_id = graphene.Field(PokemonType,id=graphene.String(required=True))

    def resolve_all_pokemons(self, info, **kwargs):
        return Pokemon.objects.all()

    def resolve_pokemon_by_id(self,info,id):
        try:
            return Pokemon.objects.get(pokemon_id=id)
        except Pokemon.DoesNotExist:
            return 404


schema = graphene.Schema(query=Query)
