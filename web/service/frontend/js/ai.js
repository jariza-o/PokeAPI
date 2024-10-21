const button = document.querySelector(".bobobo");
button.addEventListener('click', function(){
    const pokemonName = document.getElementById('pokemonName').value;
    const pokemonType = document.getElementById('pokemonType').value;
    const accessory = document.getElementById('accessory').value;
    const prompt = document.getElementById('prompt').value;

    const generatedPrompt = `Create a ${pokemonType} type Pokémon named ${pokemonName} that has a ${accessory}. Prompt: ${prompt}`;

    document.getElementById('generatedPrompt').innerText = generatedPrompt;
})