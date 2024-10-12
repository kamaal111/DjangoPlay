from django.contrib.auth.models import User
from django.db import models


class BlogManager(models.Manager): ...


class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    content = models.TextField()
    is_draft = models.BooleanField(default=False)
    date_published = models.DateTimeField(default=None, null=True)
    date_edited = models.DateTimeField(default=None, null=True)

    objects = BlogManager()

    def __str__(self) -> str:
        return f"({self.pk}) {self.title}"
