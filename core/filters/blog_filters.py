from django_filters import rest_framework as filters


class BlogFilter(filters.FilterSet):
    title = filters.CharFilter()


    class Meta:
        model = Blog
        filters = ['title']


class BlogerFilter(filters.FilterSet):
    first_name = filters.CharFilter()
    second_name = filters.CharFilter()

    class Meta:
        model = Bloger
        filters = ['first_name', 'second_name']