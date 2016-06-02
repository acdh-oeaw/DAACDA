from rest_framework import serializers
from .models import Label


class LabelSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Label
