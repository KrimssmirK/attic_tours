from django.db import models


def create_choices(model):
    items_on_db = model.objects.all()
    choices = {str(item_name)[0]: str(item_name) for item_name in items_on_db}
    return choices

class VisaType(models.Model):
    visa_type = models.CharField(max_length=200)
    
    def __str__(self):
        return self.visa_type


class Coordinator(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    

class Report(models.Model):
    visa_type = models.CharField(max_length=1, choices=create_choices(VisaType), default="")
    coordinator = models.CharField(max_length=1, choices=create_choices(Coordinator), default="")
    report_date = models.DateTimeField("date reported")
    
    def __str__(self):
        return self.visa_type
    