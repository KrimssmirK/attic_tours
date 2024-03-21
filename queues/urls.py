from django.urls import path
from queues.views.api_like_views.queue_api import get_queue, change_number_queue, change_window_queue, change_call_queue

app_name = "queues"
urlpatterns = [
    # path("", views.queue, name="queue"),
    # path("customer/", views.customer_queue, name="customer_queue"),
    # api calls below
    path("api/get_queue/<str:service>/", get_queue, name="api_get_queue"),
    path("api/change_number_queue/<int:queue_id>/<str:str_number>/", change_number_queue, name="api_change_number_queue"),
    path("api/change_window_queue/<int:queue_id>/<str:str_number>/", change_window_queue, name="api_change_window_queue"),
    path("api/change_call_queue/<int:queue_id>/<str:switch>/", change_call_queue, name="api_change_call_queue"),
]