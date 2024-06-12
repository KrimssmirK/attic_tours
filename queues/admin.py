from django.contrib import admin
from queues.models import (
    Branch, Service, Report, Window, Queue, PrefQueue, Newsfeed, QueueSettingStatus
    )


class BranchAdmin(admin.ModelAdmin):
    list_display = ["name", "mobile_no", "landline_no"]
    
class ReportAdmin(admin.ModelAdmin):
    list_display = ["branch", "by", "service", "pax", "date"]
    list_filter = ["branch", "date"]

class ServiceAdmin(admin.ModelAdmin):
    list_display = ["name", "price"]
    
class PrefQueueAdmin(admin.ModelAdmin):
    list_display = ["branch", "service"]
    list_filter = ["branch"]
    
class NewsfeedAdmin(admin.ModelAdmin):
    list_display = ["branch", "text"]
    list_filter = ["branch"]

class QueueSettingStatusAdmin(admin.ModelAdmin):
    list_display = ["branch", "change"]


admin.site.register(Branch, BranchAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(Window)
admin.site.register(Queue)
admin.site.register(PrefQueue, PrefQueueAdmin)
admin.site.register(Newsfeed, NewsfeedAdmin)
admin.site.register(QueueSettingStatus, QueueSettingStatusAdmin)