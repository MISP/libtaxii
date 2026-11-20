@echo off
setlocal
cd /d "%~dp0"

if "%~1"=="doctest" (
    python -m sphinx -b doctest . _build/doctest
    exit /b
)

if "%~1"=="preview" (
    python render_api.py && quarto preview .
    exit /b
)

if "%~1"=="html" (
    python render_api.py && quarto render .
    exit /b
)

echo Usage: make.bat html ^| doctest ^| preview
exit /b 1
