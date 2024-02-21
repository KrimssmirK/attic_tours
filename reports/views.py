from django.shortcuts import render
from .models import Report, VisaType, Coordinator



def index(request):
    reports = Report.get_current_reports()
    visa_types = VisaType.objects.all()        
    context = {"reports": reports, "visa_types": visa_types}
    return render(request, "reports/index.html", context)


def reports(request):
    return render(request, "reports/reports.html", {})

