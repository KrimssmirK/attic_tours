from queues.default_data.services import services
from queues.default_data.branches import branches
from queues.default_data.windows import windows
from queues.default_data.pref_queues import pref_queues
from queues.default_data.newsfeeds import newsfeeds


def add_initial_service_data(apps, schema_editor):
    Service = apps.get_model("queues", "Service")
    for service in services:
        if service["price"] is None:
            Service.objects.create(name=service["name"])
        else:
            Service.objects.create(name=service["name"], price=service["price"])


def add_initial_branch_data(apps, schema_editor):
    Branch = apps.get_model("queues", "Branch")
    for branch in branches:
        Branch.objects.create(
            name=branch["name"],
            mobile_no=branch["mobile_no"],
            landline_no=branch["landline_no"],
            password=branch["password"],
        )


def add_initial_window_data(apps, schema_editor):
    Window = apps.get_model("queues", "Window")
    for window in windows:
        Window.objects.create(name=window["name"])


def add_initial_pref_queue_data(apps, schema_editor):
    PrefQueue = apps.get_model("queues", "PrefQueue")
    for pref_queue in pref_queues:
        PrefQueue.objects.create(
            service_id=pref_queue["service"],
            branch_id=pref_queue["branch"]
        )


def add_initial_newsfeed_data(apps, schema_editor):
    Newsfeed = apps.get_model("queues", "Newsfeed")
    for newsfeed in newsfeeds:
        Newsfeed.objects.create(
            text=newsfeed["text"],
            branch_id=newsfeed["branch"]
        )
