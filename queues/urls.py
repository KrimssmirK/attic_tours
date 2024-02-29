from django.urls import path
from . import views

app_name = "queues"
urlpatterns = [
    path("visa/", views.japan_visa_customer_queue, name="japan_visa_customer_queue"),
    path("worker/", views.japan_visa_worker, name="japan_visa_worker"),
    # api calls below
    path("visa/japan_queue_number", views.get_japan_queue_number, name="japan_queue_number"),
    path("visa/increase_japan_queue_number", views.put_increase_japan_queue_number, name="increase_japan_queue_number"),
    path("visa/decrease_japan_queue_number", views.put_decrease_japan_queue_number, name="decrease_japan_queue_number"),
]