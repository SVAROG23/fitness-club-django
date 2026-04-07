@echo off
echo Starting Fitness Club Django Server...
py manage.py makemigrations
py manage.py migrate
py manage.py runserver
pause
