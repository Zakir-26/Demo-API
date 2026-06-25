from django.urls import path
from . import views

name = "api"


urlpatterns = [
    path("", views.studentapi, name="studapi")
]