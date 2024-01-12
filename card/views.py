from rest_framework import generics
from .models import Card
from .serilizers import CardSerializer


class ListCard(generics.ListAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
