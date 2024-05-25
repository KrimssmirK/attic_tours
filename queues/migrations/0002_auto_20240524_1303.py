# Generated by Django 5.0.6 on 2024-05-24 05:03

from django.db import migrations
from queues.default_data import default_data


class Migration(migrations.Migration):
    dependencies = [
        ("queues", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(default_data.add_initial_service_data),
        migrations.RunPython(default_data.add_initial_branch_data),
        migrations.RunPython(default_data.add_initial_window_data),
        migrations.RunPython(default_data.add_initial_pref_queue_data),
        migrations.RunPython(default_data.add_initial_newsfeed_data),
    ]