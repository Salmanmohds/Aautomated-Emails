from django.db import models

class Employee(models.Model):
    employee_id = models.IntegerField()
    name = models.CharField(max_length=100)
    birthday = models.DateField()
    work_anniversary = models.DateField()


class EmployeeEmailTemplate(models.Model):
    event_type = models.CharField(max_length=50, unique=True)
    subject = models.CharField(max_length=100)
    body = models.TextField()
    