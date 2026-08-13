from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg.openapi import Info
from rest_framework import permissions

schema_view = get_schema_view(
    Info(
        title="DRF B18.3 API",
        default_version="v1",
        description="API documentation for 18.3 ",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0)),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0)),
]