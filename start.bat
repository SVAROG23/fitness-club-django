@echo off
title Fitness Club Server - Медведь
color 0A
echo ========================================
echo   Фитнес-центр "Медведь"
echo   Запуск сервера...
echo ========================================
echo.

REM Проверка наличия Python
python --version > nul 2>&1
if errorlevel 1 (
    echo ОШИБКА: Python не установлен!
    echo Скачайте с https://www.python.org/downloads/
    pause
    exit /b 1
)

REM Установка зависимостей
echo [1/4] Установка зависимостей...
pip install -r requirements.txt -q

REM Применение миграций
echo [2/4] Применение миграций базы данных...
python manage.py makemigrations users clients workouts schedule analytics > nul 2>&1
python manage.py migrate > nul 2>&1

REM Создание суперпользователя
echo [3/4] Создание суперпользователя...
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@fitclub.ru', 'admin123')" > nul 2>&1

REM Загрузка начальных данных (упражнения)
echo [4/4] Загрузка базы упражнений...
python manage.py shell -c "from workouts.models import Exercise; Exercise.objects.count() == 0 and Exercise.objects.bulk_create([Exercise(name='Жим лежа', muscle_group='chest'), Exercise(name='Приседания', muscle_group='legs'), Exercise(name='Становая тяга', muscle_group='back'), Exercise(name='Подтягивания', muscle_group='back'), Exercise(name='Отжимания', muscle_group='chest'), Exercise(name='Выпады', muscle_group='legs'), Exercise(name='Жим стоя', muscle_group='shoulders'), Exercise(name='Тяга штанги в наклоне', muscle_group='back'), Exercise(name='Скручивания', muscle_group='core'), Exercise(name='Планка', muscle_group='core')])" > nul 2>&1

echo.
echo ========================================
echo   СЕРВЕР ЗАПУЩЕН!
echo ========================================
echo   Сайт: http://127.0.0.1:8000
echo   Админка: http://127.0.0.1:8000/admin
echo   Логин: admin
echo   Пароль: admin123
echo ========================================
echo   Для остановки сервера нажмите Ctrl+C
echo ========================================
echo.

python manage.py runserver

pause
