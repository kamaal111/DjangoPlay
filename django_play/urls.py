from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from django_play.accounts import views as accounts_views
from django_play.blogs import views as blogs_views
from django_play.exceptions import handle_not_found

accounts_router = routers.DefaultRouter()
accounts_router.register(r"accounts", accounts_views.UserViewSet)

blogs_router = routers.DefaultRouter()
blogs_router.register(r"blogs", blogs_views.BlogViewSet)


handler404 = handle_not_found

urlpatterns = [
    path("api/", include(accounts_router.urls)),
    path("api/", include(blogs_router.urls)),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("admin/", admin.site.urls),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "docs/",
        SpectacularSwaggerView.as_view(
            template_name="swagger-ui.html", url_name="schema"
        ),
        name="swagger-ui",
    ),
]
