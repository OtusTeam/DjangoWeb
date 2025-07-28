from django.test import TestCase, Client, SimpleTestCase


class TestIndexView(SimpleTestCase):

    def test_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_context(self):
        response = self.client.get('/')
        context = response.context
        self.assertIn('param', context)
        self.assertEqual('value', context['param'])

    def test_content(self):
        response = self.client.get('/')
        content = response.content
        # print(type(content))
        # print(content)
        self.assertIn(b'Welcome to Zoo!', content)
        self.assertIn('Welcome to Zoo!', content.decode('utf-8'))
        self.assertContains(response, 'Welcome to Zoo!', 1, 200)
