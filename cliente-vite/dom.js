<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lista de Pokemons</title>

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="./src/index.css">
</head>
<body>
    <div class="container mt-5">
        <h1 class="text-center mb-4">Lista de Pokemons</h1>

        <div class="row" id="pokemon-cards"></div>


    <div class="modal fade" id="pokemonModal" tabindex="-1" aria-labelledby="pokemonModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="pokemonModalLabel">Detalhes do Pokémon</h5>
                </div>
                <div class="modal-body" id="modal-content">
                    Carregando detalhes...
                </div>
            </div>
        </div>
    </div>

    <!-- Adicionando o Bootstrap JS e o script principal -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
    <script type="module" src="./src/main.js"></script>
</body>
</html>