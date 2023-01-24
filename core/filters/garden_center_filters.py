from django_filters import rest_framework as filters
from garden_center.models import Plant, Garden_center
from core.enums.garden_center_enums import Currency, StatusOfPlant


class PlantFilter(filters.FilterSet):
    price = filters.RangeFilter()
    currency = filters.ChoiceFilter(
        choices = Currency.choices,
    )
    status = filters.ChoiceFilter(
        choices = StatusOfPlant.choices,
    )

    class Meta:
        model = Plant
        fields = ['price', 'currency', 'status']


class Garden_centerFilter(filters.FilterSet):
    plants = filters.CharFilter()


    class Meta:
        model = Garden_center
        fields = ['title', 'plants']
