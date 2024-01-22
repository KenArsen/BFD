#!/bin/sh

python manage.py migrate

python manage.py collectstatic --no-input

# Create a user
python manage.py shell -c "from django.contrib.auth import get_user_model; \
User = get_user_model(); \
User.objects.create_superuser('bfd_user', 'bfd@gmail.com', 'bfd_password') if not User.objects.filter(username='bfd_user').exists() else None"

# Start Gunicorn
exec /bin/sh -c "gunicorn --bind :8000 conf.wsgi:application"


chmod +x commands.sh