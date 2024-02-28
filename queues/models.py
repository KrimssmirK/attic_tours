from django.db import models

# Create your models here.
class Queue(models.Model):
    current_number = models.IntegerField(default=0)
    date = models.DateTimeField("queue date", auto_now=True)