from core.filters.founder_filters import FounderFilter
from core.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from garden_center.api.v1.serializers.founder_serializer import FounderSerializer
from garden_center.api.v1.views.garden_center_view import APIListPagination
from garden_center.models import Founder
from rest_framework import viewsets


class FounderViewSet(viewsets.ModelViewSet):
    queryset = Founder.objects.all()
    serializer_class = FounderSerializer
    pagination_class = APIListPagination
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend]
    filterset_class = FounderFilter
