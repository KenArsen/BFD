from celery import shared_task
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from card.models import Card


@shared_task
def send_email_async(card_id):
    try:
        card = Card.objects.get(pk=card_id)
        html_message = render_to_string('data.html', {'card': card})
        plain_message = strip_tags(html_message)

        email = EmailMultiAlternatives(
            subject=card.company_name,
            body=plain_message.strip(),
            from_email=settings.EMAIL_HOST_USER,
            to=['tan.me4nik@gmail.com']
        )

        attach_file(email, card.file)
        attach_file(email, card.signature)

        email.attach_alternative(html_message, 'text/html')

        # Send email
        email.send()

    except Card.DoesNotExist:
        # Handle the case where the card with the given ID does not exist
        pass


def attach_file(email, file_field):
    if file_field:
        email.attach(file_field.name, file_field.read())
