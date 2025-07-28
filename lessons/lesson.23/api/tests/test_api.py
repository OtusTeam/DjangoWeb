from mixer.backend.django import mixer
from rest_framework.test import APITestCase, APIClient
from mainapp.models import Category
from userapp.models import MyUser
from api.serializers import CategorySerializer


class CategoryViewSetAPITestCase(APITestCase):

    def setUp(self):
        user = MyUser.objects.create_user('user', 'user@user.com', 'user')
        self.client.force_authenticate(user=user)
        self.guest_client = APIClient()
        self.admin_client = APIClient()
        user = MyUser.objects.create_superuser('admin', 'admin@admin.com', 'admin')
        self.admin_client.force_authenticate(user=user)

    def test_list_status_code(self):
        response = self.client.get('/api/categories/')
        self.assertEqual(200, response.status_code)

    def test_list_status_code_guest(self):
        response = self.guest_client.get('/api/categories/')
        self.assertEqual(401, response.status_code)

    def test_list_empty_response(self):
        response = self.client.get('/api/categories/')
        self.assertEqual(
            {'count': 0, 'next': None, 'previous': None, 'results': []},
            response.json()
        )
        self.assertEqual(response.json()['results'], [])

    def test_list_response(self):
        one = mixer.blend(Category, name='Медведь')
        mixer.blend(Category, name='Тигр')
        response = self.client.get('/api/categories/')

        print('DEBUG')
        print(response.json()['results'][0]['create'])
        print(one.create)
        print('end debug')

        self.assertEqual(
            {
             'count': 2,
             'next': 'http://testserver/api/categories/?page=2',
             'previous': None,
             'results': [
                 # {
                 #     'name': one.name,
                 #     'id': one.id,
                 #     'create': one.create,
                 #     'create_duplicated': one.create_duplicated,
                 # }
                 CategorySerializer(one).data
             ]
             },
            response.json()
        )

        # self.assertJSONEqual(
        #     response.content,
        #     {
        #      'count': 2,
        #      'next': 'http://testserver/api/categories/?page=2',
        #      'previous': None,
        #      'results': [
        #          {
        #              'name': one.name,
        #              'id': one.id,
        #              'create': one.create,
        #              'create_duplicated': one.create_duplicated,
        #          }
        #      ]
        #      }
        # )

    def test_create(self):
        data = {
            'name': 'New animal'
        }
        self.assertFalse(Category.objects.all().exists())
        response = self.client.post(
            '/api/categories/',
            data=data,
            format='json',
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(1, Category.objects.all().count())
        self.assertEqual('New animal', Category.objects.first().name)
