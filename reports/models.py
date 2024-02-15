from django.db import models


class Report(models.Model):
    visa_type = models.CharField(max_length=200)
    coordinator = models.CharField(max_length=200)
    no_of_pax = models.IntegerField(default=1, choices=((i,i) for i in range(1, 101)))
    report_date = models.DateTimeField("date reported")
    
    def __str__(self):
        return self.visa_type
    
    
class VisaType(models.Model):
    visa_type = models.CharField(max_length=200)
    
    def __str__(self):
        return self.visa_type
    
    
class Coordinator(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
