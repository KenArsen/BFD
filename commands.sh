#!/bin/sh
exec /bin/sh -c "python manage.py migrate && \
      python manage.py collectstatic --no-input && \
      gunicorn --bind :8000 conf.wsgi:application"

chmod +x commands.sh