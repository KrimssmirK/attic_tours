from django.urls import path
from . import views

app_name = "queues"
urlpatterns = [
    path("japan/", views.japan_queue_view_customer, name="japan_visa_queue_view_for_customer"),
    path("japan/worker", views.japan_queue_view_worker, name="japan_visa_queue_view_for_worker"),
    # api calls below
    path("japan/get_current_queue_number", views.get_japan_queue_number, name="get_current_queue_number_japan")
]