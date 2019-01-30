#!/bin/bash

py="python"
py3="python3"

python=""
if command -v $py >/dev/null 2>&1; then
    python="$py"
elif command -v $py3 > /dev/null 2>&1; then
    python="$py3"
else
    echo "python command is required for this script."
    exit 1
fi

echo "Delete all history on this django project."
find . -type d -name "migrations" -exec rm -rf {} \;

# TODO: init the django-system database
$python manage.py migrate

$python manage.py makemigrations wx_user
$python manage.py makemigrations sweepstake
$python manage.py makemigrations participate

$python manage.py migrate