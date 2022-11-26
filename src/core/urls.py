from core import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("news/", views.news, name="news"),
    path("downloads/", views.downloads, name="downloads"),
    path("warframes/", views.warframes, name="warframes"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
]
