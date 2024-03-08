from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 
from django.utils import timezone


class Window(models.Model):
    number = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    service_type = models.CharField(default="Japan Visa", max_length=200)
    
    def __str__(self):
        return str(self.number) + " (" + self.service_type + ")"
    


class Queue(models.Model):
    current_queue_number = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    window = models.ForeignKey(Window, on_delete=models.CASCADE)
    call = models.BooleanField(default=False)
    date = models.DateTimeField("queue date", default=timezone.now)
    

