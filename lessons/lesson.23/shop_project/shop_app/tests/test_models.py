from django.test import TestCase, SimpleTestCase


class TestModel(SimpleTestCase):

    def test_sum(self):
        self.assertEqual(10, 6 + 4)
