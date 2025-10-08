from django.test import TestCase
# import requests

class SimpleAPITest(TestCase):
    def test_api_home(self):
        response = self.client.get('http://127.0.0.1:8000')  # Django's internal client
        print(response.status_code)
        print(response.content)
        self.assertEqual(response.status_code, 200)
