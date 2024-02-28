from django.db import models


class Queue(models.Model):
    current_queue_number = models.IntegerField(default=0)
    date = models.DateTimeField("queue date", auto_now=True)