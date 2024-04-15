from django.urls import path
from branch.views import branch_select, login_branch

app_name = "branch"
urlpatterns = [
    path("", branch_select, name="branch_select"),
    path("login/", login_branch, name="login_branch")
]