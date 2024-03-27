from django.contrib import admin
from .models import Queue, Service


class QueueAdmin(admin.ModelAdmin):
    list_display = ["branch", "service", "number", "window", "call", "date"]
    list_filter = ["branch", "date"]


admin.site.register(Queue, QueueAdmin)
admin.site.register(Service)
