from rest_framework import viewsets

from garden_center.api.v1.serializers.category_serializer import CategorySerializer
from garden_center.api.v1.views.garden_center_view import APIListPagination
from garden_center.models import Category
from core.permissions import IsAdminOrReadOnly


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('title')
    serializer_class = CategorySerializer
    pagination_class = APIListPagination
    permission_classes = (IsAdminOrReadOnly,)
    search_fields = ['title']