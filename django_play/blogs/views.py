from rest_framework import mixins, viewsets

from .models import Blog
from .serializers import BlogSerializer


class BlogViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    """
    API endpoint that allows blogs to be viewed, edited, listed or deleted.
    """

    queryset = Blog.objects.all().order_by("id")
    serializer_class = BlogSerializer
