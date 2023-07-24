from first.api import RegisterApi
from django.urls import path

urlpatterns = [
    path("api/register/", RegisterApi.as_view(), name="register"),
]
