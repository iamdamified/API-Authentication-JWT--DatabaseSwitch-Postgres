from django.urls import path
from . import views



urlpatterns = [
    path("jwtcore/", views.api_home_page, name="jwtcore")
]