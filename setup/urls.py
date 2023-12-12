"""setup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication


SchemaView = get_schema_view(
    openapi.Info(
        title="Urano API",
        default_version="v1",
        description="API para expor os dados do sistema FinanceControl",
        terms_of_service="https://github.com/hilton98/financeControl",
        contact=openapi.Contact(email="hiltoncosta98@gmail.com"),
    ),
    public=True,
    authentication_classes=[JWTAuthentication],
    permission_classes=[permissions.AllowAny],
    validators=["ssv"],
)


urlpatterns = [
    path(
        "admin/",
        admin.site.urls
    ),
    re_path(
        r'^swagger(?P<format>\.json|\.yaml)$',
        SchemaView.without_ui(cache_timeout=0),
        name='schema-json'
    ),
    path(
        'swagger/',
        SchemaView.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'
    ),
    path(
        'redoc/',
        SchemaView.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'
    ),
    path("financial/", include("apps.financial.urls")),
    path("userinfo/", include("apps.userinfo.urls")),
]
