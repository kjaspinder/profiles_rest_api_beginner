#!/usr/bin/env bash

set -e

PROJECT_BASE_PATH='/usr/local/apps/profiles_rest_api_beginner'

git pull
$PROJECT_BASE_PATH/env/bin/python manage.py migrate
$PROJECT_BASE_PATH/env/bin/python manage.py collectstatic --noinput
supervisorctl restart profiles_api

echo "DONE! :)"
