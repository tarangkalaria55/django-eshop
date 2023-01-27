from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("account/", include("allauth.urls")),
    path("", include("core.urls")),
]
