from . import views
from django.urls import path


urlpatterns = [
    path("User/", views.User.as_view(), name="User"),
    path("Login/", views.Login.as_view(), name="Login")
]