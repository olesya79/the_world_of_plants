from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from core.permissions import AllowAny

from garden_center.api.v1.serializers.plant_serializer import PlantSerializer
from garden_center.api.v1.views.garden_center_view import APIListPagination
from garden_center.models import Plant
from core.filters.garden_center_filters import PlantFilter


class PlantViewSet(viewsets.ModelViewSet):
    queryset = Plant.objects.all().order_by('time_create')
    serializer_class = PlantSerializer
    pagination_class = APIListPagination
    permission_classes = (AllowAny,)
    filter_backends = [DjangoFilterBackend]
    filterset_class = PlantFilter
    search_fields = ['title', 'kind']
    ordering_fields = ['title']