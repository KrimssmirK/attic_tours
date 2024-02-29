from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 


class Queue(models.Model):
    current_queue_number = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    date = models.DateTimeField("queue date", auto_now=True)