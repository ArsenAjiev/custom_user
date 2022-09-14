#!/bin/bash



## Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Start server
echo "Starting server"
gunicorn custom_user.wsgi:application -w 4 -b :8000 --log-level debug
#python manage.py runserver 0.0.0.0:8000
