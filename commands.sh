#!/bin/sh

python manage.py migrate

python manage.py collectstatic --no-input

# Create a user
#python manage.py shell -c "from django.contrib.auth import get_user_model; \
#User = get_user_model(); \
#User.objects.get_or_create(username='bfd_user', \
#    defaults={'password': 'bfd_password', 'email': 'bfd@gmail.com', 'is_staff': True, 'is_superuser': True})"

# Start Gunicorn
exec /bin/sh -c "gunicorn --bind :8000 conf.wsgi:application"


chmod +x commands.sh