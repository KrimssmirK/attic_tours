from django.urls import path
from . import views

app_name = "queues"
urlpatterns = [
    path("", views.queue, name="queue"),
    path("customer/", views.customer_queue, name="customer_queue"),
    # api calls below
    path("visa/japan_korea_ticket_queue_number", views.get_japan_korea_ticket_queue, name="japan_korea_ticket_queue"),
    # japan
    path("visa/increase_japan_queue_number", views.put_increase_japan_queue_number, name="increase_japan_queue_number"),
    path("visa/decrease_japan_queue_number", views.put_decrease_japan_queue_number, name="decrease_japan_queue_number"),
    path("visa/call_japan_applicant", views.call_japan_applicant, name="call_japan_applicant"),
    path("visa/set_japan_window", views.set_japan_window, name="set_japan_window"),
    # korea ticket
    path("visa/increase_korea_ticket_queue_number", views.put_increase_korea_ticket_queue_number, name="increase_korea_ticket_queue_number"),
    path("visa/decrease_korea_ticket_queue_number", views.put_decrease_korea_ticket_queue_number, name="decrease_korea_ticket_queue_number"),
    path("visa/call_korea_ticket_applicant", views.call_korea_ticket_applicant, name="call_korea_ticket_applicant"),
    path("visa/set_korea_ticket_window", views.set_korea_ticket_window, name="set_korea_ticket_window")
]