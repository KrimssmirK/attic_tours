from django.urls import path
from queues.views.views_home import home

app_name = "queues"
urlpatterns = [
    path("", home, name="home")
]