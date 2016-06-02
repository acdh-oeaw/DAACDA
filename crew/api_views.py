from rest_framework import viewsets
from .serializers import PersonSerializer
from .models import Person


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    depth = 2
