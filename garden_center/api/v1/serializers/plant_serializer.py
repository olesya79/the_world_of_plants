from rest_framework import serializers

from garden_center.models import Plant


class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ['title', 'kind', 'price', 'currency']