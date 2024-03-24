from django.contrib import admin
from .models import ReportType, Report


class ReportAdmin(admin.ModelAdmin):
    list_display = ["branch", "coordinator", "report_type", "no_of_pax", "report_date"]
    list_filter = ["branch", "report_date"]

admin.site.register(ReportType)
admin.site.register(Report, ReportAdmin)
