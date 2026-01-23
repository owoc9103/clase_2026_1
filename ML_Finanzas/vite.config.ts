import { defineConfig } from 'vite'

export default defineConfig({
  server: {
    port: 3030,
  },
  // Asegurar que las rutas relativas funcionen correctamente
  resolve: {
    alias: {
      '@': '/',
    },
  },
})
