from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    content = models.TextField()
    is_draft = models.BooleanField()
    date_published = models.DateTimeField(default=None, null=True)
    date_edited = models.DateTimeField(default=None, null=True)

    def __str__(self) -> str:
        return f"({self.pk}) {self.title}"
