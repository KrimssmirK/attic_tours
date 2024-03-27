from django.db import models

class Branch(models.Model):
    name = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=30)
    landline_no = models.CharField(max_length=30)
    
    class Meta:
        db_table = "branch"
        verbose_name_plural = "branches"
        
    def __str__(self):
        return self.name
