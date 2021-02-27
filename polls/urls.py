from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="BING"),
    path("meme/", views.meme, name="meme")
]
