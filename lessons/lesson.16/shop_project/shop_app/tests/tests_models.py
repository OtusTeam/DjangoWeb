from django.test import TestCase
from shop_app.models import Product, Category


class ModelsTestCase(TestCase):

    def setUp(self):
        # print('я выполняюсь перед каждым тестом')
        self.category = Category.objects.create(
            name='Books'
        )

    def tearDown(self):
        # print('я выполняюсь после каждого теста')
        pass

    def test_category_str(self):
        self.assertEqual(str(self.category), 'Books')

    def test_product_str(self):
        product = Product.objects.create(
            title='Fight club',
            price=2.00,
        )

        product.categories.add(self.category)
        product.save()

        self.assertEqual(str(product), 'Fight club')
