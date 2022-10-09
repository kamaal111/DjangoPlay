from rest_framework import mixins, viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema


from .models import Blog
from .serializers import BlogSerializer, CreatePayloadSerializer
from .services import BlogsService


class BlogViewSet(
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

    @extend_schema(request=CreatePayloadSerializer)
    def create(self, request: Request, *args, **kwargs):
        payload_serializer = CreatePayloadSerializer(data=request.data)
        payload_serializer.is_valid(raise_exception=True)

        blogs_service = BlogsService()
        blog = blogs_service.create(
            **payload_serializer.data,
        )

        serialized_blog: BlogSerializer = self.get_serializer(blog)
        return Response(serialized_blog.data, status=200)
