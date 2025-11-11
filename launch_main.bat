@echo off
REM --- Ce script lance main.py avec le python.exe specifique du venv ---

REM --- IMPORTANT : Nom de votre environnement virtuel ---
SET VENV_NAME=myenv

REM --- Obtient le chemin du répertoire où se trouve ce script .bat ---
SET "PROJECT_ROOT=%~dp0"

REM --- Construit le chemin complet vers l'EXECUTABLE Python du venv ---
SET "PYTHON_EXE=%PROJECT_ROOT%%VENV_NAME%\Scripts\python.exe"

REM --- Construit le chemin complet vers le script Python ---
SET "PYTHON_SCRIPT=%PROJECT_ROOT%main.py"

REM --- Vérifie si l'executable python.exe du venv existe ---
if not exist "%PYTHON_EXE%" (
    echo ERREUR: Le fichier python.exe est introuvable.
    echo Chemin recherche : %PYTHON_EXE%
    echo Verifiez que VENV_NAME est correct.
    pause
    goto :eof
)

echo Lancement du script Python avec l'interpreteur de %VENV_NAME%...
REM --- Lance le script Python EN UTILISANT L'EXECUTABLE SPECIFIQUE DU VENV ---
"%PYTHON_EXE%" "%PYTHON_SCRIPT%"

echo Script termine.

REM --- Optionnel: pause pour voir la sortie en cas de double-clic manuel ---
REM --- Commentez la ligne "pause" ci-dessous pour le Task Scheduler ---
REM pause

:eof