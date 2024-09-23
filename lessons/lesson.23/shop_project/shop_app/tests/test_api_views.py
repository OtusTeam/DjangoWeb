from django.contrib.auth.models import User
from shop_app.api_views import CategoryViewSet
from shop_app.models import Category
from rest_framework.test import APITestCase, APIRequestFactory, APIClient


class CategoriesApiAPITestCase(APITestCase):

    def setUp(self):
        user = User.objects.create_user(username='user', email='user@user.com', password='user123')
        self.client.force_authenticate(user=user)
        guest_client = APIClient()
        self.guest_client = guest_client

    def test_status_list_guest_code(self):
        url = '/api/shop/categories/'
        response = self.guest_client.get(url)
        self.assertEqual(401, response.status_code)

    def test_status_list_code(self):
        url = '/api/shop/categories/'
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)

    def test_data_list_empty(self):
        url = '/api/shop/categories/'
        response = self.client.get(url)
        result = []
        self.assertEqual(result, response.json())

    def test_data_list(self):
        category_data = [
            ('cat', 'cat desc'),
            ('dog', 'dog desc')
        ]

        for name, desc in category_data:
            Category.objects.create(name=name, description=desc)

        url = '/api/shop/categories/'
        response = self.client.get(url)
        result = [
            {
                'id': 1,
                'name': 'cat',
                'description': 'cat desc',
            },
            {
                'id': 2,
                'name': 'dog',
                'description': 'dog desc',
            },
        ]
        self.assertEqual(result, response.json())

    def test_status_create(self):
        url = '/api/shop/categories/'
        data = {
                'name': 'cat',
                'description': 'cat desc',
            }
        response = self.client.post(url, data=data)
        self.assertEqual(201, response.status_code)

        self.assertTrue(Category.objects.filter(name='cat').exists())

        url = '/api/shop/categories/'
        response = self.client.get(url)
        data['id'] = 1
        result = [
            data,
        ]
        self.assertEqual(result, response.json())

    # def test_with_factory(self):
    #     factory = APIRequestFactory()
    #     view = CategoryViewSet.as_view({'get': 'list'})
    #     request = factory.get('/api/shop/categories/')
    #     response = view(request)
    #     self.assertEqual(response.status_code, 200)
