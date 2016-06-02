from rest_framework import serializers
from labels.serializers import LabelSerializer
from .models import Place


class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    alternative_name = LabelSerializer(many=True)

    class Meta:
        model = Place
