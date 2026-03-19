@echo off
REM Ejecuta la app Streamlit usando el entorno virtual del proyecto
cd /d "%~dp0"
if exist "..\..\..\.venv\Scripts\streamlit.exe" (
    "..\..\..\.venv\Scripts\streamlit.exe" run Home.py
) else (
    echo Instalando dependencias...
    "..\..\..\.venv\Scripts\pip.exe" install -r requirements.txt -q
    "..\..\..\.venv\Scripts\streamlit.exe" run Home.py
)
