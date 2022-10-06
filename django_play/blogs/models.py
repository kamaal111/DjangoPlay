from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    date_published = models.DateTimeField(default=None, null=True)
    date_edited = models.DateTimeField(default=None, null=True)
