@echo off
title Фитнес-центр «Медведь»
color 0A

echo ========================================
echo    Фитнес-центр «Медведь»
echo    Запуск сервера...
echo ========================================
echo.

cd /d "C:\Users\user\Desktop\ВКР\fitness-club-django"

echo [1/4] Активация виртуального окружения...
call venv\Scripts\activate.bat

echo [2/4] Создание миграций...
py -3.12 manage.py makemigrations

echo [3/4] Применение миграций...
py -3.12 manage.py migrate

echo [4/4] Запуск сервера...
echo.
echo Сервер запущен! Откройте в браузере: http://127.0.0.1:8000
echo Для остановки сервера закройте это окно или нажмите Ctrl+C
echo ========================================
echo.

py -3.12 manage.py runserver

pause
