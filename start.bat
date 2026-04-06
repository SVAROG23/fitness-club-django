@echo off
cd /d "C:\Users\user\Desktop\ВКР\fitness-club-django"
call venv\Scripts\activate.bat
py -3.12 manage.py runserver
pause
