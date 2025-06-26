from django.test import TestCase
from http import HTTPStatus

class ProductsCategoryViewTests(TestCase):
    def test_products_category_view(self):
        response = self.client.get('/products/category/')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'shop_app/category_products.html')

