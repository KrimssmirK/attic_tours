from django.shortcuts import render
from .models import Report, VisaType, Coordinator
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy



def index(request):
    reports = Report.get_current_reports()
    visa_types = VisaType.objects.all()        
    context = {"reports": reports, "visa_types": visa_types}
    return render(request, "reports/index.html", context)


class ReportPageView(CreateView):
  model = Report
  template_name = 'reports/reports.html'
  fields = "__all__"
  success_url = reverse_lazy('reports:index')
  

