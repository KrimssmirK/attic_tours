from django.urls import path
from queues.views.views_home import home, login
from queues.views.views_report import report, api_send_report
from queues.views.views_queue import queue
from queues.views.views_feedback import feedback
from queues.views.views_applicant_queue import applicant_queue

app_name = "queues"
urlpatterns = [
    # home
    path("", home, name="home"),
    path("login/", login, name="login"),
    # report
    path("branch/<int:branch_id>/report/", report, name="report"),
    path("branch/api/send_report/", api_send_report, name="api_send_report"),
    # queue
    path("branch/<int:branch_id>/queue/", queue, name="queue"),
    # feedback
    path("branch/<int:branch_id>/feedback/", feedback, name="feedback"),
    # applicant's queue
    path("branch/<int:branch_id>/applicant_queue/", applicant_queue, name="applicant_queue"),
]