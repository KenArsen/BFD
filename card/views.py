import os
import zipfile
from io import BytesIO

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from rest_framework import generics, status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Card
from .serializers import CardSerializer


class HealthCheckView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"status": "OK"}, status=status.HTTP_200_OK)


class CardList(generics.ListAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class CardDetail(generics.RetrieveAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class CardCreate(generics.CreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        send_email(instance)


class CardUpdate(generics.UpdateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsAdminUser]

    def perform_update(self, serializer):
        updated_instance = serializer.save()
        send_email(updated_instance)


class CardDelete(generics.DestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsAdminUser]


def send_email(card):
    zip_buffer = BytesIO()
    with zipfile.ZipFile(zip_buffer, 'w') as zip_file:
        zip_file.write(card.file.path, arcname=os.path.basename(card.file.path))
        zip_file.write(card.signature.path, arcname=os.path.basename(card.signature.path))

    zip_buffer.seek(0)

    email = EmailMultiAlternatives(
        subject=card.company_name,
        body=strip_tags(render_to_string('data.html', {'card': card})),
        from_email=settings.EMAIL_HOST_USER,
        to=['Sales@bfd.com']
    )

    email.attach('file_and_signature.zip', zip_buffer.read(), 'application/zip')

    email.attach_alternative(render_to_string('data.html', {'card': card}), 'text/html')

    email.send()


def attach_file(email, file_field):
    if file_field:
        email.attach(file_field.name, file_field.file.read())
