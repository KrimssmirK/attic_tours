from django.test import TestCase
from django.urls import reverse
from queues.models import Branch

class HomeUrlsTests(TestCase):
    
    def test_url_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    
    def test_urlname_status_code(self):
        response = self.client.get(reverse("queues:home"))
        self.assertEqual(response.status_code, 200)
        

class LoginUrlsTests(TestCase):
    @classmethod
    def setUpTestData(clf):
        Branch.objects.create(
            name="SM FAIRVIEW",
            mobile_no="234234",
            landline_no="234242",
            password="1234"
        )
    
    def test_login_when_password_matched(self):
        response = self.client.post("/login/", {"branchId": "1", "password": "1234"})
        self.assertEqual(response.status_code, 200)
    
    def test_login_when_password_not_matched(self):
        response = self.client.post("/login/", {"branchId": "1", "password": "1234afd"})
        self.assertEqual(response.status_code, 200)
    
    def test_login_with_name_when_password_matched(self):
        response = self.client.post(reverse("queues:login"), {"branchId": "1", "password": "1234"})
        self.assertEqual(response.status_code, 200)
    
    def test_login_with_name_when_password_not_matched(self):
        response = self.client.post(reverse("queues:login"), {"branchId": "1", "password": "1asdfs234"})
        self.assertEqual(response.status_code, 200)