from rest_framework import serializers
from rest_framework.request import Request

from .models import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = (
            "id",
            "is_draft",
            "title",
            "content",
            "date_published",
            "date_edited",
        )

    def create(self, validated_data):
        request: Request = self.context["request"]

        return super().create({**validated_data, "user": request.user})
