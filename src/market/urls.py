from market import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("list_item/", views.list_item, name="list_item"),
    path("create_item/", views.create_item, name="create_item"),
]
