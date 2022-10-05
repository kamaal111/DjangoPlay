from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from django_play.accounts import views

accounts_router = routers.DefaultRouter()
accounts_router.register(r"accounts/users", views.UserViewSet)
accounts_router.register(r"accounts/groups", views.GroupViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(accounts_router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
