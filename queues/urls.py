from django.urls import path
from . import views

app_name = "queues"
urlpatterns = [
    path("", views.queue, name="queue"),
    path("customer/", views.customer_queue, name="customer_queue"),
    # api calls below
    path("visa/japan_queue_number", views.get_japan_queue, name="japan_queue"),
    path("visa/increase_japan_queue_number", views.put_increase_japan_queue_number, name="increase_japan_queue_number"),
    path("visa/decrease_japan_queue_number", views.put_decrease_japan_queue_number, name="decrease_japan_queue_number"),
    path("visa/call_applicant", views.call_applicant, name="call_applicant"),
    path("visa/set_window", views.set_window, name="set_window")
]