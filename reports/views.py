from django.shortcuts import render
from django.utils import timezone
from .models import Report, VisaType, Coordinator



def index(request):
    reports = Report.objects.filter(report_date__date=timezone.now().date())
    visa_types = VisaType.objects.all()
    
    # sum up each visa types
    reports_dicts = dict()
    for report in reports:
        if report.visa_type in reports_dicts:
            reports_dicts[report.visa_type] += report.no_of_pax
        else:
            reports_dicts[report.visa_type] = report.no_of_pax
    print("reports_dicts:", reports_dicts)
            
    context = {"reports": reports_dicts, "visa_types": visa_types}
    return render(request, "reports/index.html", context)

