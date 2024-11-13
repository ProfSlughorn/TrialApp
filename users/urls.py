from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),  # For the homepage
    path("input/", views.user_input, name="user-form"),  # For the user input form
]
