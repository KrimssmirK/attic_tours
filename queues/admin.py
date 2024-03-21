from django.contrib import admin
from .models import Queue, Service


class QueueAdmin(admin.ModelAdmin):
    list_display = ["service", "number", "window", "date"]
    list_filter = ["date"]


admin.site.register(Queue, QueueAdmin)
admin.site.register(Service)