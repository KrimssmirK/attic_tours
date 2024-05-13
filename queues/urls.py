from django.urls import path
from queues.views.views_home import home, login
from queues.views.views_report import report, api_send_report
from queues.views.views_queue import (
    view_queue,
    api_get_services,
    api_create_pref_queue,
    api_get_pref_queues,
    api_delete_pref_queue,
    api_read_queues,
    api_decrease_queue_no,
    api_increase_queue_no,
    api_set_queue_window,
    api_call_applicant,
    api_newsfeeds,
    api_create_newsfeed,
    api_delete_newsfeed,
    api_get_queue,
    api_reset_call_applicant,
    api_change_newsfeed,
    change_queue_setting_status,
    queue_setting_status
)
from queues.views.views_feedback import feedback, api_send_feedback
from queues.views.views_applicant_queue import applicant_queue

app_name = "queues"
urlpatterns = [
    # --------------------------------------VIEWs--------------------------------------
    # HOME
    path("", home, name="home"),
    # REPORT
    path("branch/<int:branch_id>/report/", report, name="report"),
    # QUEUE
    path("branch/<int:branch_id>/queue/", view_queue, name="queue"),
    path(
        "branch/<int:branch_id>/applicant_queue/",
        applicant_queue,
        name="applicant_queue",
    ),
    # FEEDBACK
    path("branch/<int:branch_id>/feedback/", feedback, name="feedback"),
    
    
    # --------------------------------------APIs--------------------------------------
    # HOME
    path("login/", login, name="login"),
    # REPORT
    path("branch/api/send_report/", api_send_report, name="api_send_report"),
    # QUEUE
    path("branch/api/services/", api_get_services, name="api_get_services"),
    path(
        "branch/api/create_pref_queue/",
        api_create_pref_queue,
        name="api_create_pref_queue",
    ),
    path("branch/api/pref_queues/", api_get_pref_queues, name="api_get_pref_queues"),
    path(
        "branch/api/delete_pref_queue/",
        api_delete_pref_queue,
        name="api_delete_pref_queue",
    ),
    path("branch/api/read_queues/", api_read_queues, name="api_read_queues"),
    path("branch/api/get_queue/", api_get_queue, name="api_get_queue"),
    path(
        "branch/api/decrease_queue_no/",
        api_decrease_queue_no,
        name="api_decrease_queue_no",
    ),
    path(
        "branch/api/increase_queue_no/",
        api_increase_queue_no,
        name="api_increase_queue_no",
    ),
    path(
        "branch/api/set_queue_window/",
        api_set_queue_window,
        name="api_set_queue_window",
    ),
    path("branch/api/call_applicant/", api_call_applicant, name="api_call_applicant"),
    path(
        "branch/api/reset_call_applicant/",
        api_reset_call_applicant,
        name="api_reset_call_applicant",
    ),
    path(
        "branch/api/change_queue_setting_status/",
        change_queue_setting_status,
        name="change_queue_setting_status",
    ),
     path(
        "branch/api/queue_setting_status/",
        queue_setting_status,
        name="queue_setting_status",
    ),
    # NEWSFEED
    path("branch/api/newsfeeds/", api_newsfeeds, name="api_newsfeeds"),
    path(
        "branch/api/create_newsfeed/", api_create_newsfeed, name="api_create_newsfeed"
    ),
    path(
        "branch/api/delete_newsfeed/", api_delete_newsfeed, name="api_delete_newsfeed"
    ),
    path(
        "branch/api/change_newsfeed/", api_change_newsfeed, name="api_change_newsfeed"
    ),
    # FEEDBACK
    path("branch/api/send_feedback/", api_send_feedback, name="api_send_feedback"),
]
