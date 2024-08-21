from django.test import TestCase, SimpleTestCase
from .models import Person, Manager


class ManagerTestCase(TestCase):

    def test_str(self):
        manager = Manager.objects.create(
            name="Bob",
            age=23,
            job_title='Some title',
            experience=1
        )
        self.assertEqual(str(manager), f"{manager.id} {manager.name} {manager.job_title}")


class PersonTestCase(SimpleTestCase):

    def test_str(self):
        person = Person(name="Bob", age=23)
        self.assertEqual(str(person), "Bob")
