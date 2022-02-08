"""collection URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_nested import routers


from collection.shows.api.viewsets import SeasonViewSet, ShowViewSet, EpisodeViewSet


router = routers.DefaultRouter()
router.register(r"shows", ShowViewSet)

shows_router = routers.NestedDefaultRouter(router, r"shows", lookup="show")
shows_router.register(r"seasons", SeasonViewSet)

seasons_router = routers.NestedDefaultRouter(shows_router, r"seasons", lookup="season")
seasons_router.register(r"episodes", EpisodeViewSet)



schema_view = get_schema_view(
    openapi.Info(
        title="Media Collection API",
        default_version="v1",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path(
        r"swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(r"redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("", include(router.urls)),
    path("", include(shows_router.urls)),
    path("", include(seasons_router.urls)),
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
]