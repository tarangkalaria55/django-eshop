from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

# admin site
admin.site.site_header = "E-Shop Admin"
admin.site.site_title = "E-Shop Admin Site"
admin.site.index_title = "E-Shop Admin"

urlpatterns = [
    path("", RedirectView.as_view(url=reverse_lazy("account_login")), name="login"),
    path("admin/", admin.site.urls),
    path("account/", include("allauth.urls")),
    path("account/", include("accounts.urls")),
]

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
