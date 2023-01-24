from rest_framework import viewsets
from core.permissions import IsAuthenticated
from core.filters.bloger_filters import BlogerFilter

from blog.api.v1.serializers.bloger_serializer import BlogerSerializer
from blog.api.v1.views.blog_view import APIListPaginationBlog
from supplier.models import Founder


class BlogerViewSet(viewsets.ModelViewSet):
    queryset = Bloger.objects.all()
    serializer_class = BlogerSerializer
    pagination_class = APIListPaginationBlog
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend]
    filterset_class = BlogerFilter