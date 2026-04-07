@echo off
chcp 65001 >nul
echo ========================================
echo   Fitness Club Django Server
echo ========================================
echo.

where py >nul 2>nul
if %errorlevel%==0 (
    set PYTHON_CMD=py
) else (
    set PYTHON_CMD=python
)

echo [1/3] Installing requirements...
%PYTHON_CMD% -m pip install django djangorestframework django-cors-headers

echo.
echo [2/3] Making migrations...
%PYTHON_CMD% manage.py makemigrations users
%PYTHON_CMD% manage.py makemigrations clients
%PYTHON_CMD% manage.py makemigrations workouts
%PYTHON_CMD% manage.py makemigrations schedule
%PYTHON_CMD% manage.py makemigrations analytics
%PYTHON_CMD% manage.py migrate

echo.
echo [3/3] Starting server...
echo.
echo ========================================
echo   Server started at: http://127.0.0.1:8000
echo   Admin panel: http://127.0.0.1:8000/admin
echo   Press Ctrl+C to stop
echo ========================================
echo.

%PYTHON_CMD% manage.py runserver

pause
