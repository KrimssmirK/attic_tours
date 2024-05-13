# Generated by Django 5.0.2 on 2024-05-13 06:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("queues", "0003_prefqueue"),
    ]

    operations = [
        migrations.CreateModel(
            name="QueueSettingStatus",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("change", models.BooleanField(default=False)),
                (
                    "branch",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="queues.branch"
                    ),
                ),
            ],
        ),
    ]
