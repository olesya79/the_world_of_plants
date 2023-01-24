from rest_framework import serializers

from garden_center.models import Founder

class FounderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Founder
        fields = ['first_name', 'second_name', 'contact']