from blog.api.v1.serializers.blog_serializer import BlogSerializer
from blog.models import Blog
from core.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

from core.filters.blog_filters import BlogFilter
from blog.models import Blog


class APIListPaginationBlog(PageNumberPagination):
    page_size = 5
    page_query_param = 'page_size'
    max_page_size = 10


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    pagination_class = APIListPaginationSupplier
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend]
    filterset_class = BlogFilter