from rest_framework import viewsets
from .serializers import LabelSerializer
from .models import Label


class LabelViewSet(viewsets.ModelViewSet):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer
    depth = 2
