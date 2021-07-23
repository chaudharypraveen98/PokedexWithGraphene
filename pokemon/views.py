from django.shortcuts import render


# Create your views here.
def pokemon_home(request):
    return render(request, 'pokemon/pokemon_list.html')
