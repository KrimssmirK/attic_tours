from django.urls import path
from . import views

app_name = "reports"
urlpatterns = [
    path("", views.index, name="index"),
    path("reports/", views.ReportPageView.as_view(), name="reports")
]