# 🚀 Inicio Rápido - ML Finanzas

## Instalación (Solo una vez)

```bash
# 1. Instalar dependencias Python
pip install -r requirements.txt

# 2. Instalar dependencias Node.js (Slidev)
npm install
```

## Ejecutar Presentaciones

```bash
# Desde la raíz del proyecto:

# Clase 1
npm run dev:1

# Luego abre: http://localhost:3030
```

## Comandos Útiles

```bash
# Desarrollo
npm run dev:1          # Ejecutar Clase 1

# Exportar
npm run export-pdf:1   # Exportar Clase 1 como PDF
npm run export-png:1   # Exportar Clase 1 como PNG
```

## Estructura

```
ML_Finanzas/
├── package.json       ← Configuración centralizada
├── vite.config.ts     ← Configuración Vite
├── Clases/
│   └── Clase 1/
│       └── Clase_1_Slidev.md  ← Slides
└── imagenes/          ← Recursos visuales
```

## Atajos de Teclado en Slidev

- `Space` / `→` - Siguiente slide
- `←` - Slide anterior
- `f` - Pantalla completa
- `o` - Overview de todas las slides
- `d` - Modo dibujo
- `g` - Ir a slide específica
- `?` - Ver todos los atajos

¡Listo para empezar! 🎉
