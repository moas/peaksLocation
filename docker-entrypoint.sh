#!/bin/bash
python manage.py migrate --settings=config.settings.production                 # Apply database migrations
python manage.py collectstatic --noinput --settings=config.settings.production  # Collect static files

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn config.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    --log-level=debug \
    "$@"
