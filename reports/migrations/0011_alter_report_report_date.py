# Generated by Django 5.0.2 on 2024-02-17 06:12

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("reports", "0010_alter_report_report_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="report",
            name="report_date",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="date reported"
            ),
        ),
    ]