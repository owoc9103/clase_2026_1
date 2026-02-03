# Configuración LSEG Data Library for Python

La configuración de este taller sigue el **[Quick Start](https://github.com/LSEG-API-Samples/Example.DataLibrary.Python/tree/lseg-data-examples/Quick%20Start)** del repositorio oficial [Example.DataLibrary.Python](https://github.com/LSEG-API-Samples/Example.DataLibrary.Python) (rama `lseg-data-examples`).

## Qué tener en cuenta (según Quick Start)

1. **Instalación:** `pip install lseg-data`
2. **Archivo de configuración:** Las credenciales se definen en **`Configuration/lseg-data.config.json`** (esta carpeta). No modifiques el archivo interno del paquete en site-packages; usa siempre esta copia en tu proyecto.
3. **Antes de ejecutar:** Edita **`lseg-data.config.json`** con tu App Key (y, si usas sesión Platform, usuario y contraseña). Para sesión **Desktop** (Refinitiv Workspace) solo necesitas la App Key en `desktop.workspace.app-key`.
4. **Requisitos:** Python 3.11+ recomendado; Refinitiv Workspace 1.8+ o Eikon 4.0.36+ abierto e iniciado sesión para sesión Desktop.

---

## Procedimiento para obtener la App Key

Sigue estos pasos en **Refinitiv Workspace** para generar tu App Key y usarla en `lseg-data.config.json`:

1. **Abre Refinitiv Workspace** en tu equipo e inicia sesión con tu usuario.
2. **Ve a la configuración de API / App Key:**
   - En el menú o en la barra superior busca **“API Key”**, **“App Key”** o **“Developer”** / **“Developer Portal”**.
   - O bien: menú de usuario (icono de perfil) → **Settings** / **Configuración** → sección **API** o **App Key**.
3. **Genera una nueva App Key:**
   - Pulsa **“Create App Key”** o **“Generate”** (o el botón equivalente).
   - Refinitiv mostrará un texto largo con **términos y condiciones** (uso individual, no compartir credenciales, etc.). **Es normal**; no es un error.
4. **Acepta los términos** para poder ver y copiar la clave.
5. **Copia la App Key** que aparece (cadena alfanumérica). Guárdala en un lugar seguro; a veces solo se muestra una vez.
6. **Pega la App Key en el archivo de configuración:**
   - Abre `lseg-data.config.json` en esta carpeta (`Configuration`).
   - Donde dice `"TU_APP_KEY"`, reemplázalo por tu clave real, entre comillas, por ejemplo:  
     `"app-key": "abc123tu_clave_real_xyz"`
   - Guarda el archivo.

A partir de ahí, el notebook puede usar la sesión Desktop leyendo este archivo (con Refinitiv Workspace abierto e iniciado sesión).

---

## Sesión Desktop (Refinitiv Workspace)

Si usas **Refinitiv Workspace** abierto en tu equipo:

1. Abre `lseg-data.config.json` en esta carpeta.
2. Reemplaza `"TU_APP_KEY"` por tu **App Key** real (obtenida con el procedimiento anterior).
3. No hace falta poner usuario ni contraseña en el JSON: la sesión Desktop usa la sesión ya abierta en Workspace.

**Estructura del JSON (según [repo oficial LSEG](https://github.com/LSEG-API-Samples/Example.DataLibrary.Python/blob/lseg-data-examples/Configuration/lseg-data.config.json)):** Incluye `logs` y sesión Desktop como `desktop.workspace`. Reemplaza `TU_APP_KEY` por tu App Key en `desktop.workspace.app-key`:

```json
{
  "logs": {
    "level": "debug",
    "transports": { "console": { "enabled": false }, "file": { "enabled": false } }
  },
  "sessions": {
    "default": "desktop.workspace",
    "desktop": {
      "workspace": { "app-key": "TU_APP_KEY" }
    }
  }
}
```

**Importante:** No modifiques el archivo de configuración que viene dentro del paquete instalado (site-packages). Usa siempre esta copia en la carpeta `Configuration` de tu proyecto.

---

**Más información:** [Quick Start - Example.DataLibrary.Python](https://github.com/LSEG-API-Samples/Example.DataLibrary.Python/tree/lseg-data-examples/Quick%20Start) · [Configuration - lseg-data.config.json](https://github.com/LSEG-API-Samples/Example.DataLibrary.Python/blob/lseg-data-examples/Configuration/lseg-data.config.json)
