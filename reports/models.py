from django.db import models
from django.utils import timezone


class VisaType(models.Model):
    visa_type = models.CharField(max_length=200)
    
    def __str__(self):
        return self.visa_type
    
    
class Coordinator(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


class Report(models.Model):
    visa_type = models.ForeignKey(VisaType,on_delete=models.CASCADE)
    coordinator = models.ForeignKey(Coordinator,on_delete=models.CASCADE)
    no_of_pax = models.IntegerField(default=1, choices=((i,i) for i in range(1, 101)))
    report_date = models.DateTimeField("date reported", auto_now=True)
    
    def get_current_reports():
        current_reports = Report.objects.filter(report_date__date=timezone.now().date())
        reports = dict()
        for report in current_reports:
            if report.visa_type in reports:
                reports[report.visa_type] += report.no_of_pax
            else:
                reports[report.visa_type] = report.no_of_pax
        return reports

    
    

