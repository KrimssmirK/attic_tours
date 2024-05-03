# Generated by Django 5.0.2 on 2024-04-19 05:25

from django.db import migrations

services = [
    {"name": "TOURISM", "price": 1680},
    {"name": "BUSINESS, CONFERENCE or CULTURAL EXCHANGE, etc.", "price": 1680},
    {"name": "VISITING RELATIVES", "price": 1680},
    {"name": "VISITING FRIENDS OR DISTANT RELATIVES", "price": 1680},
    {"name": "VISITING US MILITARY PERSONNEL", "price": 1680},
    {
        "name": "SPOUSE OR CHILD OF JAPANESE NATIONAL RESIDING IN THE PHILIPPINES",
        "price": 1680,
    },
    {"name": "TRANSIT", "price": 1680},
    {"name": "COE", "price": 3030},
    {"name": "NIKKEI-JIN", "price": None},
    {"name": "(PTAA) TOURISM", "price": None},
    {"name": "(PTAA) BUSINESS, CONFERENCE or CULTURAL EXCHANGE, etc.", "price": None},
    {"name": "(PTAA) VISITING RELATIVES", "price": None},
    {"name": "(PTAA) VISITING FRIENDS OR DISTANT RELATIVES", "price": None},
    {"name": "(PTAA) VISITING US MILITARY PERSONNEL", "price": None},
    {
        "name": "(PTAA) SPOUSE OR CHILD OF JAPANESE NATIONAL RESIDING IN THE PHILIPPINES",
        "price": None,
    },
    {"name": "(PTAA) TRANSIT", "price": None},
    {"name": "(PTAA) COE", "price": None},
    {"name": "(PTAA) NIKKEI-JIN", "price": None},
    {"name": "JAPAN VISA", "price": 1680},
    {"name": "KOREA VISA", "price": 1880},
    {"name": "TOUR PACKAGE", "price": None},
    {"name": "TICKET", "price": None},
    {"name": "TICKET (INTERNATIONAL)", "price": None},
    {"name": "TICKET (DOMESTIC)", "price": None},
    {"name": "WIFI", "price": None},
    {"name": "TRAVEL INSURANCE", "price": None},
]
branches = [
    {
        "name": "MAIN OFFICE",
        "mobile_no": "N/A",
        "landline_no": "(02)8556-6301",
        "password": "0000",
    },
    {
        "name": "SM MEGAMALL",
        "mobile_no": "0906-516-3246",
        "landline_no": "(02)8706-6030",
        "password": "1111",
    },
    {
        "name": "SM MALL OF ASIA",
        "mobile_no": "0917-631-0848",
        "landline_no": "(02)8252-0868",
        "password": "2222",
    },
    {
        "name": "SM FAIRVIEW",
        "mobile_no": "0916-618-6165",
        "landline_no": "(02)8829-0761",
        "password": "3333",
    },
    {
        "name": "SM NORTH EDSA",
        "mobile_no": "0917-898-0905",
        "landline_no": "(02)8372-3254",
        "password": "4444",
    },
    {
        "name": "SM CLARK",
        "mobile_no": "0917-305-4292",
        "landline_no": "(04)5499-7546",
        "password": "5555",
    },
    {
        "name": "SM SOUTHMALL",
        "mobile_no": "0917-186-6853",
        "landline_no": "(02)8281-8506",
        "password": "6666",
    },
    {
        "name": "SM DAVAO",
        "mobile_no": "0917-321-1328",
        "landline_no": "(08)2225-8920",
        "password": "7777",
    },
    {
        "name": "SM CEBU",
        "mobile_no": "0956-551-9834",
        "landline_no": "(03)2239-8435",
        "password": "8888",
    },
]
windows = [
    {"name": "ANY WINDOW"},
    {"name": "WINDOW 1"},
    {"name": "WINDOW 2"},
    {"name": "WINDOW 3"},
    {"name": "WINDOW 4"},
    {"name": "WINDOW 5"},
    {"name": "WINDOW 6"},
    {"name": "WINDOW 7"},
    {"name": "WINDOW VISA"},
    {"name": "WINDOW JAPAN VISA"},
    {"name": "WINDOW KOREA VISA"},
    {"name": "WINDOW TICKETING"},
    {"name": "WINDOW TOUR PACKAGE"},
    {"name": "WINDOW WIFI"},
    {"name": "WINDOW TOUR PACKAGE"},
]


def add_initial_data(apps, schema_editor):
    Service = apps.get_model("queues", "Service")
    for service in services:
        if service["price"] is None:
            Service.objects.create(name=service["name"])
        else:
            Service.objects.create(name=service["name"], price=service["price"])
    Branch = apps.get_model("queues", "Branch")
    for branch in branches:
        Branch.objects.create(
            name=branch["name"],
            mobile_no=branch["mobile_no"],
            landline_no=branch["landline_no"],
            password=branch["password"],
        )
    Window = apps.get_model("queues", "Window")
    for window in windows:
        Window.objects.create(name=window["name"])


class Migration(migrations.Migration):
    dependencies = [
        ("queues", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(add_initial_data),
    ]
