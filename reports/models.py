from django.db import models
from django.utils import timezone
# from queues.models import Branch


class ReportType(models.Model):
    report_type = models.CharField(max_length=200)
    
    def __str__(self):
        return self.report_type
    

class Report(models.Model):
    # branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    report_type = models.ForeignKey(ReportType,on_delete=models.CASCADE)
    coordinator = models.CharField(max_length=100)
    no_of_pax = models.IntegerField(default=1, choices=((i,i) for i in range(1, 101)))
    report_date = models.DateTimeField("date reported", auto_now=True)
    
    def get_current_reports(branch):
        current_reports = Report.objects.filter(branch=branch, report_date__date=timezone.now().date())
        reports = dict()
        for report in current_reports:
            if report.report_type in reports:
                reports[report.report_type] += report.no_of_pax
            else:
                reports[report.report_type] = report.no_of_pax
        return reports

    
    

