from django.urls import path
from reports.views import report, api_send_report

app_name = "reports"
urlpatterns = [
    path("<int:branch_id>/", report, name="report"),
    # like api
    path("api/send_report/", api_send_report, name="api_send_report")
]