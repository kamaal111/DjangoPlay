from django_play_migrations.blogs.model import Blog
from rest_framework import mixins, viewsets
from rest_framework.decorators import permission_classes as permission_classes_decorator
from rest_framework.permissions import IsAuthenticated

from .serializers import BlogSerializer


class BlogViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    """
    API endpoint that allows blogs to be viewed, edited, listed or deleted.
    """

    queryset = Blog.objects.all().order_by("id")
    serializer_class = BlogSerializer
    permission_classes = []

    @permission_classes_decorator([IsAuthenticated])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
