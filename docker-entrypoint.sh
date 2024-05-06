#!/bin/bash

# Apply database migrations
# echo "Apply database migrations"
# jg_ctl -D /var/lib/postgresql/data -l logfile start

python3 manage.py makemigrations
python3 manage.py migrate

# Create super user
echo "Create super user"
# python3 manage.py createsuperuser

# Start server
echo "Starting server"
python3 ./manage.py runserver 0.0.0.0:8000
