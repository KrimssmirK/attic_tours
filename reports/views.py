from django.shortcuts import render
from reports.models import Report, ReportType
from queues.models import Branch
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


def index(request):
  
    fairview_branch = Branch.objects.get(name="SM FAIRVIEW")
    fairview_reports = Report.get_current_reports(fairview_branch)
    
    moa_branch = Branch.objects.get(name="SM MOA")
    moa_reports = Report.get_current_reports(moa_branch)
    
    visa_types = ReportType.objects.all() 
           
    context = {
      "fairview_reports": fairview_reports,
      "moa_reports": moa_reports,
      "visa_types": visa_types
    }
    
    return render(request, "reports/index.html", context)


class ReportPageView(CreateView):
  model = Report
  template_name = 'reports/reports.html'
  fields = "__all__"
  success_url = reverse_lazy('reports:index')
  