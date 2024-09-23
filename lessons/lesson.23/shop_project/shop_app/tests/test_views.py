from django.test import TestCase, SimpleTestCase


class IndexViewTestCase(SimpleTestCase):

    def test_status_code(self):
        url = '/shop/'
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)

    def test_context(self):
        url = '/shop/'
        response = self.client.get(url)
        self.assertIn('some_data', response.context)
        self.assertEqual(response.context['some_data'], 'Some text')
        # self.assertEqual(200, response.context)

    def test_content(self):
        url = '/shop/'
        response = self.client.get(url)
        self.assertIn(b'Some text', response.content)
        self.assertContains(response, 'Some text', 1)