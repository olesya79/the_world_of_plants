from django_filters import rest_framework as filters
from garden_center.models import Founder


class FounderFilter(filters.FilterSet):
    first_name = filters.CharFilter()
    second_name = filters.CharFilter()
    age = filters.NumberFilter()

    class Meta:
        model = Founder
        fields = ['first_name', 'second_name', 'age']
