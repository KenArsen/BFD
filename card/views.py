from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Card
from .serializers import CardSerializer
from .tasks import send_email_async


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
        send_email_async.delay(instance.pk)


class CardUpdate(generics.UpdateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def perform_update(self, serializer):
        updated_instance = serializer.save()
        send_email_async.delay(updated_instance.pk)


class CardDelete(generics.DestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
