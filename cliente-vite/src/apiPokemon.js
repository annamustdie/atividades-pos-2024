export async function fetchPokemon(page = 1) {
    const limit = 20;
    const offset = (page - 1) * limit;
    const response = await fetch(`https://pokeapi.co/api/v2/pokemon?limit=${limit}&offset=${offset}`);
    const data = await response.json();
    return data.results; 
}

export async function fetchPokemonImage(pokemonUrl) {
    const response = await fetch(pokemonUrl);
    const data = await response.json();
    return data; 
}

export async function fetchPokemonDetails(pokemonUrl) {
    const response = await fetch(pokemonUrl);
    const data = await response.json();
    return data; 
}