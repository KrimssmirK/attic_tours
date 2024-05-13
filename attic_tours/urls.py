from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("queues.urls")),
    path("admin/", admin.site.urls),
]
