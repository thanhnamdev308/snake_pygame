REM Get Pygame version into PYGAME_VERSION variable
for /f "delims=" %%i in ('py -c "import pygame; print(pygame.__version__)"') do set PYGAME_VERSION=%%i

@echo off
setlocal enabledelayedexpansion

REM Get the first number of pygame version
for /f "tokens=1 delims=." %%a in ("%PYGAME_VERSION%") do (
    set /a major=%%a
)

REM Check if Pygame version meets requirements
if !major! LSS 2 (
    echo Pygame version does not meet requirements
    py -m pip install -r requirements.txt
) else (
    echo Pygame version meets requirements
)

cd snake_game
py main.py
