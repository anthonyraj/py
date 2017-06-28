Django

Install setup: https://docs.djangoproject.com/en/1.11/howto/windows/

django-admin startproject mysite

python manage.py runserver

#runserver on any ip for port 8000
python manage.py runserver 0:8000

python manage.py makemigrations polls
python manage.py sqlmigrate polls 0001
python manage.py migrate --list
python manage.py migrate
python manage.py shell


python manage.py makemigrations
python manage.py migrate --list
python manage.py migrate
python manage.py migrate --list

python manage.py createsuperuser
Username: anthony
Browser to localhost:8000/admin/login
	Login with the newly created superuser