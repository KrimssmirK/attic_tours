from django.contrib import admin
from queues.models import Branch, Service, Report, Window, Queue

class ReportAdmin(admin.ModelAdmin):
    list_display = ["branch", "by", "service", "pax", "date"]
    list_filter = ["branch", "date"]

admin.site.register(Branch)
admin.site.register(Service)
admin.site.register(Report, ReportAdmin)
admin.site.register(Window)
admin.site.register(Queue)