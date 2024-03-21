from django.contrib import admin
# from .models import JapanQueue, KoreaTicketQueue, Window

# Register your models here.
class QueueAdmin(admin.ModelAdmin):
    list_display = ["number", "date"]
    list_filter = ["date"]

# admin.site.register(JapanQueue, QueueAdmin)
# admin.site.register(KoreaTicketQueue, QueueAdmin)
# admin.site.register(Window)