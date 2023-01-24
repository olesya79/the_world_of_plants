from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import GenericViewSet

from garden_center.api.v1.serializers.garden_center_serializer import Garden_centerSerializer
from garden_center.models import Garden_center
from core.filters.garden_center_filters import Garden_centerFilter
from core.permissions import IsAuthenticatedOrReadOnly


class APIListPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page_size'
    max_page_size = 10


class Garden_centerViewSet(mixins.CreateModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            mixins.ListModelMixin,
                            GenericViewSet):
    queryset = Garden_center.objects.all()
    serializer_class = Garden_centerSerializer
    pagination_class = APIListPagination
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = [DjangoFilterBackend]
    filterset_class = Garden_centerFilter
    search_fields = ['title']
    ordering_fields = ['plants']