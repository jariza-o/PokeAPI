const button = document.querySelector(".bobobo");
const UNSPLASH_ACCESS_KEY = 'IyfTb8ftsg0FGPIYQSXkFS-WPmSNtXdxe2DJvM0NJWU';


button.addEventListener('click', async function(){
    const pokemonName = document.getElementById('pokemonName').value;
    const pokemonType = document.getElementById('pokemonType').value;
    const accessory = document.getElementById('accessory').value;
    const prompt = document.getElementById('prompt').value;

    const generatedPrompt = `Take me a image a ${pokemonType} type Pokémon, named ${pokemonName} that has a ${accessory}. Prompt: ${prompt}`;
    document.getElementById('generatedPrompt').innerText = generatedPrompt;

    try {
        const query = generatedPrompt;
        const response = await fetch(`https://api.unsplash.com/photos/random?query=${query}&client_id=${UNSPLASH_ACCESS_KEY}`);
        
        if (response.ok) {
          const data = await response.json();
          const imageUrl = data.urls.regular;
   
          const imageDiv = document.getElementById('unsplash-image');
          imageDiv.innerHTML = `<img src="${imageUrl}" alt="Imagen de Unsplash" style="max-width: 100%;">`;
        } else {
          console.error('Error al obtener la imagen de Unsplash:', response.statusText);
        }
      } catch (error) {
        console.error('Error en la solicitud:', error);
      }
})