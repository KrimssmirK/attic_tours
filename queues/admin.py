from django.contrib import admin
from .models import Queue

# Register your models here.
class QueueAdmin(admin.ModelAdmin):
    list_display = ["current_number", "date"]
    list_filter = ["date"]

admin.site.register(Queue, QueueAdmin)