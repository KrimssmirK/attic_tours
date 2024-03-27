from django.urls import path
from reports.views import stats, ReportPageView

app_name = "reports"
urlpatterns = [
    path("<int:branch_id>/", stats, name="stats"),
    path("<int:branch_id>/reports/", ReportPageView.as_view(), name="reports"),
]