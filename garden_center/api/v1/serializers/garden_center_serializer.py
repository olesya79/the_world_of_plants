from rest_framework import serializers

from garden_center.models import Garden_center


class Garden_centerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Garden_center
        fields = ['title', 'location', 'contact']