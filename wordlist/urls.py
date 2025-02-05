from django.urls import path
from . import views

app_name = "wordlist"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("deleat/", views.delete, name="deleat"),
    path("input/<int:id>/", views.input, name="input"),
    path("input/<int:id>/add/", views.add_post, name="add_post"),
    path("delete_post/<int:post_id>/", views.delete_post, name="delete_post"),
]
