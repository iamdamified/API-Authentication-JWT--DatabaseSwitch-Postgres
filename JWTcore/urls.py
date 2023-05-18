from django.urls import path
from . import views
from .views import create_student, all_student, new_registration



urlpatterns = [
    path("jwtcore/", views.api_home_page, name="jwtcore"),
    path('register/', create_student, name='register'),
    path('students/', all_student, name='students'),
    path('frontend_new_registration/', new_registration, name='frontend_new_registration')
]