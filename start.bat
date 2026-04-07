@echo off
title Fitness Club Server
echo Starting Fitness Club Server...
echo.

REM Активируем виртуальное окружение (если оно есть)
if exist venv\Scripts\activate (
    call venv\Scripts\activate
)

REM Проверяем и устанавливаем зависимости
pip install -r requirements.txt > nul 2>&1
echo Dependencies checked.

REM Применяем миграции базы данных
python manage.py makemigrations > nul 2>&1
python manage.py migrate > nul 2>&1
echo Database migrated.

REM Создаем суперпользователя (если не создан)
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@example.com', 'admin123')" > nul 2>&1
echo Admin user: admin / admin123

REM Запускаем сервер
echo.
echo ========================================
echo Server is starting...
echo Open in browser: http://127.0.0.1:8000
echo Admin panel: http://127.0.0.1:8000/admin
echo Login: admin / admin123
echo ========================================
echo.
python manage.py runserver

pause
