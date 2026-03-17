# -*- coding: utf-8 -*-
"""
Componente reutilizable para preguntas con Enviar respuesta y Ampliar más.
Optimiza el caché mostrando feedback solo tras enviar.
"""

import streamlit as st


def pregunta_con_ampliar(
    key_prefix: str,
    pregunta: str,
    opciones: list,
    correcta: str,
    explicacion_correcta: str,
    explicacion_incorrecta: str,
    ejemplos_notebook,
) -> None:
    """
    Muestra una pregunta con botón Enviar respuesta y sección Ampliar más.
    
    ejemplos_notebook: lista de dicts con "titulo" y "codigo" para cada bloque copiable.
    """
    respuesta = st.radio(pregunta, opciones, key=key_prefix + "_radio", index=None)
    
    col_btn, _ = st.columns([1, 3])
    with col_btn:
        enviado = st.button("📤 Enviar respuesta", key=key_prefix + "_btn")
    
    if enviado and respuesta is not None:
        if respuesta == correcta:
            st.success("✅ Correcto")
            st.caption(explicacion_correcta)
        else:
            st.error("❌ Incorrecto")
            st.caption(explicacion_incorrecta)
        
        # Sección Ampliar más (solo tras enviar)
        with st.expander("📚 Ampliar más: ejemplos para copiar al notebook", expanded=False):
            st.markdown("Copia cada bloque (usa el botón **Copy** en la esquina) en una celda de tu notebook de Python:")
            for i, ej in enumerate(ejemplos_notebook, 1):
                st.markdown(f"**Ejemplo {i}: {ej['titulo']}**")
                if ej.get("explicacion"):
                    st.caption(ej["explicacion"])
                st.code(ej["codigo"], language="python")
                st.markdown("---")
