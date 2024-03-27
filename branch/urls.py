from django.urls import path
from branch.views import branch_select

app_name = "branch"
urlpatterns = [
    path("", branch_select, name="branch_select"),
]