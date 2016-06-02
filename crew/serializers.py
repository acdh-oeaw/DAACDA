from rest_framework import serializers
from bomber.serializers import BomberSerializer
from .models import Person


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    bomber = BomberSerializer(many=False)

    class Meta:
        model = Person
