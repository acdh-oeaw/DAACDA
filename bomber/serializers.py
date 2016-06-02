from rest_framework import serializers
from places.serializers import PlaceSerializer
from .models import Bomber


class BomberSerializer(serializers.HyperlinkedModelSerializer):
    crash_place = PlaceSerializer(many=False)
    last_seen = PlaceSerializer(many=False)
    crash_place = PlaceSerializer(many=False)

    class Meta:
        model = Bomber
