from django.test import TestCase, SimpleTestCase
from mainapp.models import Category, Animal
from mixer.backend.django import mixer

class TestCategory(TestCase):

    def test_some(self):
        self.assertEqual(1, 1)

    def test_str(self):
        category = Category.objects.create(name='some name')
        self.assertEqual(str(category), 'some name')


class TestAnimal(TestCase):

    def test_get_category_name(self):
        # category = mixer.blend(Category, name='some name')
        # animal = mixer.blend(Animal, category=category)

        animal = mixer.blend(Animal, category__name='some name')
        self.assertEqual(animal.get_category_name(), 'some name')
