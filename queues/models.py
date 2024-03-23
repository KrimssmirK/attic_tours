from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "service"

    def __str__(self):
        return self.name

    def convert_attrbs_to_dict(self):
        return {"id": self.id, "name": self.name}


class Queue(models.Model):
    number = models.PositiveSmallIntegerField("current number", default=0)
    window = models.PositiveSmallIntegerField("current window", default=0)
    call = models.BooleanField("is calling?", default=False)
    date = models.DateField("created", auto_now_add=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    class Meta:
        db_table = "queue"

    def __str__(self):
        return self.service.name + " " + "Queue"

    def convert_attrbs_to_dict(self):
        return {
            "id": self.id,
            "number": self.number,
            "window": self.window,
            "call": self.call,
        }
