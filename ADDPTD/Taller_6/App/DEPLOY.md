# Despliegue en Streamlit Community Cloud

## Problema: espacio en la ruta

La carpeta `Taller 6` tiene un espacio en el nombre. Esto provoca un error al instalar dependencias porque la ruta `ADDPTD/Taller 6/App/requirements.txt` se interpreta incorrectamente como `6/App/requirements.txt`.

## Solución

**Usa la ruta alternativa sin espacios** en la configuración de tu app en Streamlit Cloud:

- **Ruta incorrecta:** `ADDPTD/Taller 6/App/Home.py`
- **Ruta correcta:** `ADDPTD/Taller_6/App/Home.py`

La carpeta `Taller_6` es un enlace a `Taller 6`, por lo que ambos paths apuntan a los mismos archivos.

## Pasos para actualizar

1. Entra a [share.streamlit.io](https://share.streamlit.io)
2. Abre tu app
3. Settings → Main file path
4. Cambia a: `ADDPTD/Taller_6/App/Home.py`
5. Guarda y redespliega

## Alternativa: renombrar la carpeta

Si `Taller_6` no funciona (p. ej. el enlace no se sube bien a Git):

1. Cierra Streamlit y cualquier programa que use la carpeta.
2. Renombra `ADDPTD/Taller 6` → `ADDPTD/Taller_6`.
3. En Streamlit Cloud, configura la ruta: `ADDPTD/Taller_6/App/Home.py`.
4. Haz commit y push de los cambios.
