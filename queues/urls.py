from django.urls import path
from queues.views.worker_view import worker_queue
from queues.views.api_like_views.service_api import get_services
from queues.views.api_like_views.queue_api import get_queue, change_number_queue, change_window_queue, change_call_queue

app_name = "queues"
urlpatterns = [
    path("", worker_queue, name="worker_queue"),
    # path("customer/", views.customer_queue, name="customer_queue"),
    # SERVICE API
    path("api/services/", get_services, name="api_services"),
    # QUEUE API
    path("api/get_queue/<str:service>/", get_queue, name="api_get_queue"),
    path("api/change_number_queue/<int:queue_id>/<str:str_number>/", change_number_queue, name="api_change_number_queue"),
    path("api/change_window_queue/<int:queue_id>/<str:str_number>/", change_window_queue, name="api_change_window_queue"),
    path("api/change_call_queue/<int:queue_id>/<str:switch>/", change_call_queue, name="api_change_call_queue"),
]