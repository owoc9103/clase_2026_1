# Angry Birds Académico — NumPy (itch.io)

Juego HTML5 para publicar en [itch.io](https://itch.io/) como **juego web / HTML**.

## Cómo subirlo

1. Comprime el contenido de esta carpeta (`index.html`, `game.js`, `styles.css`, y la carpeta **`media/`** con el `.mp3`) en un `.zip`.

   **Importante:** el botón **Guardar resultados (PDF)** usa **jsPDF** desde CDN (cdnjs). Sin conexión, el juego ofrece un JSON de respaldo. Para itch.io hace falta red al cargar la página la primera vez (o empaqueta `jspdf.umd.min.js` localmente).
2. En itch.io: **Dashboard → Crear nuevo proyecto → Kind: HTML**.
3. Sube el zip. Asegúrate de que la página principal sea `index.html` (es el valor por defecto).

## Contenido pedagógico

Las preguntas están alineadas con la teoría de **Clase 6 — NumPy** (`FundProg/Notebooks/Clase_6_Teoría_Numpy.ipynb`): `ndarray`, `zeros`, producto `*` vs `@`, broadcasting, `arange`, `linspace`, `numpy.linalg`, vistas/`reshape`, `np.save`.

## Nota (3 a 5, pasos 0,2)

Combina eficiencia de **lanzamientos** (ideal: uno por pregunta) y **tiempo total**. La fórmula está en `game.js` (`computeGrade` / `gradeFromScore`). Al terminar puedes **Guardar resultados** (descarga un JSON).

Las preguntas salen en **orden aleatorio** cada partida desde `QUESTIONS_BANK` (comandos típicos de la clase de NumPy).

## Identificación del jugador

- **Nombre**: lo escribe al inicio.
- **ID de sesión**: UUID en `sessionStorage` (persiste en el mismo navegador).
- **Huella de entorno**: idioma, zona horaria, resolución y fragmento de user-agent.

**No** se puede obtener la **IP pública** solo con JavaScript en el navegador. Para eso haría falta un servidor (API) o un servicio externo.

## Audio

La música de fondo es el archivo **`media/djartmusic-i-love-my-8-bit-game-console-301272.mp3`**, reproducido en bucle con `<audio>`. Asegúrate de tener **derechos de uso** de la pista según su licencia (p. ej. uso docente / royalty-free del autor).

Durante la partida aparece el botón flotante **Música** para silenciar o reactivar.

## Exportación PDF

Al guardar resultados, el PDF incluye la **fecha y hora de exportación en hora de Colombia** (`America/Bogota`, la oficial en el país). El nombre del archivo lleva un sello `YYYYMMDDHHmmss` en esa misma zona horaria.

## Prueba local

Abre `index.html` en el navegador (doble clic) o sirve la carpeta con un servidor estático, por ejemplo:

```bash
python -m http.server 8080
```

Luego visita `http://localhost:8080/Juego_numpy/` según la ruta donde ejecutes el comando.
