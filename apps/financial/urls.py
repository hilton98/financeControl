from . import views
from django.urls import path


urlpatterns = [
    path("Institution/", views.Institution.as_view(), name="Institution")
]
