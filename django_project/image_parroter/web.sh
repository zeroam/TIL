#!/bin/sh

until psql -h "db" -U "postgres" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done
>&2 echo "Postgres is up - executing command"

python manage.py migrate --noinput && python manage.py makemigrations && python manage.py runserver 0.0.0.0:8000
