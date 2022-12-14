from market import views
from django.urls import path

urlpatterns = [
    path("", views.list_item, name="index"),
    path("list_item/", views.list_item, name="list_item"),
    path("create_item/", views.create_item, name="create_item"),
    path("delete_item/", views.delete_item, name="delete_item"),
    path("get_item/<str:slug>/", views.get_item, name="get_item"),
    path("edit_item/<str:slug>/", views.edit_item, name="edit_item"),
]
