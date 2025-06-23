from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)

class Manager(Person):
    expirience = models.IntegerField(default=0)
    job_title = models.CharField(max_length=200)

