@echo off
cd /d "C:\Users\user\Desktop\ВКР\fitness-club-django"
call venv\Scripts\activate.bat
python -3.12 manage.py runserver
pause
