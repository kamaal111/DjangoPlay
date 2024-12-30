from django.contrib import admin
from django_play_migrations.blogs.model import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin): ...
