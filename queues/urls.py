from django.urls import path
from queues.views.views_home import home, login
from queues.views.views_report import report, api_send_report
from queues.views.views_queue import queue, api_get_services, api_create_pref_queue, api_get_pref_queues, api_delete_pref_queue
from queues.views.views_feedback import feedback
from queues.views.views_applicant_queue import applicant_queue

app_name = "queues"
urlpatterns = [
    path("", home, name="home"),
    path("login/", login, name="login"),
    path("branch/<int:branch_id>/report/", report, name="report"),
    path("branch/api/send_report/", api_send_report, name="api_send_report"),
    path("branch/<int:branch_id>/queue/", queue, name="queue"),
    path("branch/api/services/", api_get_services, name="api_get_services"),
    path("branch/api/create_pref_queue/", api_create_pref_queue, name="api_create_pref_queue"),
    path("branch/api/pref_queues/", api_get_pref_queues, name="api_get_pref_queues"),
    path("branch/api/delete_pref_queue/", api_delete_pref_queue, name="api_delete_pref_queue"), # NEW
    path("branch/<int:branch_id>/feedback/", feedback, name="feedback"),
    path("branch/<int:branch_id>/applicant_queue/", applicant_queue, name="applicant_queue"),
]