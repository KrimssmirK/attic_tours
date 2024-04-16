from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.name


class Branch(models.Model):
    name = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=50)
    landline_no = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    
    class Meta:
        verbose_name_plural = "branches"
    
    def __str__(self):
        return self.name


class Report(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    pax = models.PositiveIntegerField(default=1)
    by = models.CharField(max_length=100)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.service) + " " + str(self.pax)
    

class Window(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name


class Queue(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    no = models.PositiveIntegerField(default=0)
    window = models.ForeignKey(Window, on_delete=models.SET_NULL, null=True, blank=True)
    call = models.BooleanField(default=False)
    date = models.DateField(auto_now=True)
    
    def __str__(self):
        return f"{self.branch}-{self.service}-{self.no}-{self.window}"
    

class Newsfeed(models.Model):
    text = models.CharField(max_length=200)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.text[:10]
    

class Feedback(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.branch}-{self.title}"
    