from market import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("create_item", views.create_item, name="create_item"),
]
