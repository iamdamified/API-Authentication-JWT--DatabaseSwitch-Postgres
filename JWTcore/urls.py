from django.urls import path
from . import views
from .views import create_student



urlpatterns = [
    path("jwtcore/", views.api_home_page, name="jwtcore"),
    path('register/', create_student, name='register')
]