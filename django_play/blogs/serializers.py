from rest_framework import serializers

from .models import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = [
            "id",
            "user_id",
            "is_draft",
            "title",
            "content",
            "date_published",
            "date_edited",
        ]


class CreatePayloadSerializer(serializers.Serializer):
    token = serializers.CharField(required=True)
    title = serializers.CharField(min_length=1, max_length=128, required=True)
    content = serializers.CharField(required=True)
    is_draft = serializers.BooleanField(default=False, required=False)
    date_published = serializers.DateTimeField(default=None, required=False)
    date_edited = serializers.DateTimeField(default=None, required=False)

    class Meta:
        fields = [
            "token",
            "title",
            "content",
            "is_draft",
            "date_published",
            "date_edited",
        ]
