from django.urls import path
from . import views

urlpatterns = [
    # goes to views file and find the index function
    path("", views.index, name="index"),
]
