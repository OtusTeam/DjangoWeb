from mixer.backend.django import mixer
from django.test import TestCase
from shop_app.models import Product, Category, OrderProduct


class ModelsTestCase(TestCase):

    def setUp(self):
        # print('я выполняюсь перед каждым тестом')
        self.category = mixer.blend(Category, name='Books')

    def tearDown(self):
        # print('я выполняюсь после каждого теста')
        pass

    def test_category_str(self):
        self.assertEqual(str(self.category), 'Books')

    def test_product_str(self):
        product = mixer.blend(Product, title='Fight club')
        self.assertEqual(str(product), 'Fight club')

    def test_order_product_str(self):
        order_product = mixer.blend(OrderProduct)
        self.assertEqual(str(order_product), f'{order_product.id}')

    def test_get_order_user_big_name(self):
        order_product = mixer.blend(OrderProduct, order__user__username='biguser')
        self.assertEqual(order_product.get_order_user_big_name(), 'BIGUSER')
