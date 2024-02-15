from django.contrib import admin
from .models import VisaType, Coordinator, Report


class ReportAdmin(admin.ModelAdmin):
    list_display = ["report_date", "visa_type", "no_of_pax", "coordinator"]
    list_filter = ["report_date"]

admin.site.register(VisaType)
admin.site.register(Coordinator)
admin.site.register(Report, ReportAdmin)
