from datetime import datetime
from typing import TYPE_CHECKING, Optional

from django_play.accounts.services import AuthenticationService

from .serializers import BlogSerializer

if TYPE_CHECKING:
    from .models import Blog


class BlogsService:
    def __init__(self) -> None:
        ...

    def create(
        self,
        token: str,
        title: str,
        content: str,
        is_draft: bool,
        date_published: Optional[datetime],
        date_edited: Optional[datetime],
    ):
        authentication_service = AuthenticationService()
        authenticated_token = authentication_service.authenticated_token(token=token)

        serialized_blog = BlogSerializer(
            data={
                "user_id": authenticated_token.user,
                "title": title,
                "content": content,
                "is_draft": is_draft,
                "date_published": date_published,
                "date_edited": date_edited,
            }
        )
        serialized_blog.is_valid(raise_exception=True)

        created_blog: Blog = serialized_blog.create(
            validated_data={**serialized_blog.data, "user": authenticated_token.user}
        )
        return created_blog
