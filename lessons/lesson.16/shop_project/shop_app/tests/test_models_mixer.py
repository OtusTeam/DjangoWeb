# from mixer.backend.django import mixer
from django.test import TestCase
from shop_app.models import Product, Category
from faker import Faker
from random import randint

class TestModels(TestCase):
    '''def _test_product(self): # For use you will need install mixer
        product = mixer.blend(Product)
        self.assertIsNotNone(product.title)
        print('-'*50)
        print(product.title, product.price, product.description)'''
    
    def test_product_faker(self):
        fake = Faker(locale='en_US')
        product = Product.objects.create(
            title=fake.name(),
            price=fake.pyfloat(left_digits=2, right_digits=2, positive=True),
            description=fake.text(),
        )
        self.assertIsInstance(
            product.price, float
        )