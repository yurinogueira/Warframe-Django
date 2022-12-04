from product import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("list_product/", views.list_product, name="list_product"),
    path("create_product/", views.create_product, name="create_product"),
    path("edit_product/", views.edit_product, name="edit_product"),
    path("delete_product/", views.delete_product, name="delete_product"),
]
