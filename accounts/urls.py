# i created this file
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
]
