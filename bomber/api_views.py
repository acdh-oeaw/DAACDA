from rest_framework import viewsets
from .serializers import BomberSerializer
from .models import Bomber


class BomberViewSet(viewsets.ModelViewSet):
    queryset = Bomber.objects.all()
    serializer_class = BomberSerializer
    depth = 2
