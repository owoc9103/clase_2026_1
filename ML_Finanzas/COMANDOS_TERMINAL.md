# 🖥️ Guía de Comandos de Terminal - Slidev

## ⚠️ Problema: No puedo escribir en la terminal

Cuando ejecutas `npm run dev:1` o `slidev`, el proceso se ejecuta y **ocupa la terminal**. Esto es normal y esperado.

## ✅ Soluciones

### Opción 1: Salir de Slidev (Recomendado)

Mientras Slidev está corriendo, puedes usar estos atajos:

- **`q`** - Quit (Salir) - Cierra Slidev y libera la terminal
- **`r`** - Restart (Reiniciar) - Reinicia el servidor
- **`o`** - Open (Abrir) - Abre en el navegador
- **`e`** - Edit (Editar) - Abre el archivo en el editor

**Para salir y poder escribir de nuevo:**
1. Presiona `q` en la terminal donde está corriendo Slidev
2. O presiona `Ctrl+C` (funciona en cualquier momento)

### Opción 2: Abrir una Nueva Terminal

Si necesitas usar la terminal mientras Slidev corre:

1. En VS Code: Presiona `` Ctrl+Shift+` `` (backtick) para abrir una nueva terminal
2. O ve a: `Terminal` → `New Terminal`
3. Ahora tienes dos terminales: una con Slidev corriendo y otra libre para comandos

### Opción 3: Ejecutar en Segundo Plano (PowerShell)

En PowerShell, puedes ejecutar Slidev en segundo plano:

```powershell
# Ejecutar en segundo plano
Start-Process npm -ArgumentList "run dev:1" -NoNewWindow

# O usar el operador &
npm run dev:1 &
```

## 📋 Comandos Útiles Durante la Ejecución

Mientras Slidev está corriendo, puedes usar estos atajos directamente en la terminal:

| Tecla | Acción |
|-------|--------|
| `q` | Salir de Slidev |
| `r` | Reiniciar el servidor |
| `o` | Abrir en navegador |
| `e` | Editar el archivo de slides |
| `Ctrl+C` | Forzar cierre (si `q` no funciona) |

## 🔄 Flujo de Trabajo Recomendado

### Para Desarrollar/Editar:

1. **Terminal 1**: Ejecuta Slidev
   ```bash
   npm run dev:1
   ```

2. **Terminal 2**: Úsala para otros comandos (git, npm, etc.)

3. **Navegador**: Abre `http://localhost:3030` para ver los cambios en tiempo real

4. **Editor**: Edita `Clase_1_Slidev.md` - los cambios se reflejan automáticamente

### Para Solo Ver la Presentación:

1. Ejecuta: `npm run dev:1`
2. Abre el navegador en `http://localhost:3030`
3. Cuando termines, presiona `q` en la terminal para salir

## 🐛 Problemas Comunes

### "No puedo escribir nada"

**Causa**: Slidev está corriendo y ocupa la terminal.

**Solución**: 
- Presiona `q` para salir
- O `Ctrl+C` para forzar cierre
- O abre una nueva terminal

### "El puerto 3030 está en uso"

**Causa**: Ya hay una instancia de Slidev corriendo.

**Solución**:
```powershell
# Encontrar y cerrar el proceso
Get-Process -Name node | Stop-Process

# O cambiar el puerto en vite.config.ts
```

### "Los cambios no se reflejan"

**Causa**: El servidor necesita reiniciarse.

**Solución**: 
- Presiona `r` en la terminal donde corre Slidev
- O sal (`q`) y vuelve a ejecutar `npm run dev:1`

## 💡 Tips

1. **Usa dos terminales**: Una para Slidev, otra para comandos
2. **Hot Reload**: Los cambios en `.md` se reflejan automáticamente - no necesitas reiniciar
3. **Atajo rápido**: `q` es más rápido que `Ctrl+C` para salir
4. **Modo Presentación**: Usa `http://localhost:3030/presenter/` para ver notas del presentador

## 📚 Recursos

- [Documentación de Slidev](https://sli.dev)
- [Guía de Comandos de Slidev](https://sli.dev/guide/commands.html)

---

**Recuerda**: Cuando Slidev está corriendo, la terminal está "ocupada". Esto es normal. Usa `q` para salir o abre una nueva terminal.
