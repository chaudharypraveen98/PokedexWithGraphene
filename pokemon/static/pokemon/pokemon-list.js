$(function () {

    'use strict';
    $.ajax({
        type: 'POST',
        url: '../graphql/',
        contentType: "application/json",
        data: JSON.stringify({
            query: "{  allPokemons{    pokemonId    pokemonUrl    pokemonName    pokemonImageUrl  pokemonTag{ tag }}}"
        }),
        success: function (data) {
            for (let i = 0; i < data['data']['allPokemons'].length; i++) {
                const pokemon = data['data']['allPokemons'][i];
                $(".pokemon-container").append(`
                    <div class="pokemon-card">
                        <img src="${pokemon['pokemonImageUrl']}" class="card-img-top" alt="pokemon image">
                        <div class="pokemon-body">
                          <h5 class="pokemon-title">${pokemon['pokemonName']}</h5>
                          <h3 class="pokemon-id">${pokemon['pokemonId']}</h3>
                          <h4 class="pokemon-tags">${pokemon['pokemonTag'][0]['tag']}</h4>                        
                        <div class="pokemon-link">
                            <a href="${pokemon['pokemonUrl']}" class="pokemon-button">More Details</a>
                        <div>
                        </div>
                      </div>`
                );
            }
        },
        error: function (error_data) {
            console.log(error_data['responseText'])
        }
    })
});