from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Manager(Person):
    job_title = models.CharField(max_length=100)
    experience = models.IntegerField()

    def __str__(self):
        return f"{self.id} {self.name} {self.job_title}"


# clark = Person.objects.get(name="Clark")
# print(clark)
# clark_manager = clark.manager
# print(clark_manager)
