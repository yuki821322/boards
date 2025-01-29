from django.urls import path
from . import views

app_name = "wordlist"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("deleat/", views.delete, name="deleat"),
]
