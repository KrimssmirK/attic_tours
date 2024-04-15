from django.test import TestCase
from django.urls import reverse

class HomeUrlsTests(TestCase):
    
    def test_url_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    
    def test_urlname_status_code(self):
        response = self.client.get(reverse("queues:home"))
        print(reverse("queues:home"))
        self.assertEqual(response.status_code, 200)