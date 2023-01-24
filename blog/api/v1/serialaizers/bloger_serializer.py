from rest_framework import serializers

from blog.models import Bloger

class BlogerSerializers(serializers.ModelSerializers):
    class Meta:
        model = Bloger
        fields = ['first_name', 'second_name', 'email', 'location']