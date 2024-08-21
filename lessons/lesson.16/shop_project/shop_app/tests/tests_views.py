from http import HTTPStatus
from django.test import TestCase


class CategoriesMinListViewTestCase(TestCase):

    def test_status_code(self):
        url = '/shop/categories-min/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
