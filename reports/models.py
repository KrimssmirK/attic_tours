from django.db import models

class Visa(models.Model):
    visa_type = models.CharField(max_length=200)
    
    def __str__(self):
        return self.visa_type
