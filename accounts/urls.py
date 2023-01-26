from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import HomeView

app_name = "accounts"

urlpatterns = [
    path("home/", HomeView.as_view(), name="home"),
]
