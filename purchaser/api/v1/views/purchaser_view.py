from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from core.permissions import IsAuthenticated

from core.filters.purchaser_filters import PurchaserFilter
from purchaser.api.v1.serializers.purchaser_serializer import PurchaserSerializer
from purchaser.api.v1.views.balance_view import APIListPaginationPurchaser
from purchaser.models import Purchaser


class PurchaserViewSet(viewsets.ModelViewSet):
    queryset = Purchaser.objects.all()
    serializer_class = PurchaserSerializer
    pagination_class = APIListPaginationPurchaser
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend]
    filterset_class = PurchaserFilter
    search_fields = ['first_name', 'second_name']
