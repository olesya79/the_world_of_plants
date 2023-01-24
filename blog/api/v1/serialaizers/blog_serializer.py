from rest_framework import serializers

from blog.models import Blog

class BlogSerializers(serializers.ModelSerializers):
    class Meta:
        model = Blog
        fields = ['title']