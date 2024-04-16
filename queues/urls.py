from django.urls import path
from queues.views.views_home import home, login

app_name = "queues"
urlpatterns = [
    path("", home, name="home"),
    path("login/", login, name="login"),
]