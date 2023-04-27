from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from django_play.accounts import views as accounts_views
from django_play.blogs import views as blogs_views
from django_play.exceptions import handle_not_found


accounts_router = routers.DefaultRouter()
accounts_router.register(r"accounts", accounts_views.UserViewSet)

blogs_router = routers.DefaultRouter()
blogs_router.register(r"blogs", blogs_views.BlogViewSet)


handler404 = handle_not_found

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(accounts_router.urls)),
    path("", include(blogs_router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "docs/",
        SpectacularSwaggerView.as_view(
            template_name="swagger-ui.html", url_name="schema"
        ),
        name="swagger-ui",
    ),
]
