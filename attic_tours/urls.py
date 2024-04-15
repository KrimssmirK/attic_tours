from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path("", include("branch.urls")),
    # path("branch/", include("reports.urls")),
    # path("branch/", include("queues.urls")),
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),  # new
]
