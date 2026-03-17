# Despliegue en itch.io

Este juego esta listo para publicarse como proyecto **HTML / browser playable** en `itch.io`.

## Archivos que debes subir

Comprime en un `.zip` estos archivos dejando `index.html` en la raiz:

- `index.html`
- `styles.css`
- `app.js`
- `README_ITCHIO.md` (opcional, no es necesario para que funcione)

## Pasos en itch.io

1. Crea un nuevo proyecto en [itch.io](https://itch.io/).
2. En tipo de proyecto, selecciona juego HTML o navegador.
3. Sube el archivo `.zip`.
4. Marca la opcion:
   - `This file will be played in the browser`
5. Si `itch.io` te pide dimensiones iniciales del viewport, puedes usar:
   - ancho: `1280`
   - alto: `800`
6. Guarda y prueba el juego en vista previa.

## Recomendaciones

- Activa pantalla completa si quieres una experiencia mas cercana a concurso de TV.
- Como el audio se genera con Web Audio API, el jugador debe interactuar con el boton de audio para activarlo.
- El historial local usa `localStorage`, asi que funciona por navegador, no como ranking global compartido.

## Si quieres multijugador real online

Para que varios computadores compartan partidas o ranking en tiempo real, necesitas agregar un backend, por ejemplo:

- Firebase
- Supabase
- un servidor propio con WebSockets
