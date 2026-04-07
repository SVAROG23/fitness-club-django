@echo off
echo Starting Fitness Club Django Server...
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
pause
