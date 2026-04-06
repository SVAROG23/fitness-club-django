@echo off
title Фитнес-центр «Медведь»
color 0A

echo ========================================
echo    Фитнес-центр «Медведь»
echo    Запуск сервера...
echo ========================================
echo.

cd /d "C:\Users\user\Desktop\ВКР\fitness-club-django"

echo [1/5] Активация виртуального окружения...
call venv\Scripts\activate.bat

echo [2/5] Создание миграций...
py -3.12 manage.py makemigrations --noinput

echo [3/5] Применение миграций...
py -3.12 manage.py migrate --noinput

echo [4/5] Создание суперпользователя (если не существует)...
echo from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@example.com', 'admin123') | py -3.12 manage.py shell

echo [5/5] Запуск сервера...
echo.
echo ========================================
echo    СЕРВЕР ЗАПУЩЕН!
echo    Откройте браузер: http://127.0.0.1:8000
echo    Админ-панель: http://127.0.0.1:8000/admin
echo    Логин: admin  Пароль: admin123
echo ========================================
echo.
echo Для остановки сервера закройте это окно
echo ========================================
echo.

py -3.12 manage.py runserver

pause
