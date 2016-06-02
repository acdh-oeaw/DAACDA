from rest_framework import viewsets
from .serializers import PlaceSerializer
from .models import Place


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    depth = 2
