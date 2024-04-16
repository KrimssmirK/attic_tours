from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from queues.views.views_home import home, login
from queues.models import Branch
import json


class HomeViewTests(TestCase):
    
    @classmethod
    def setUpTestData(clf):
        Branch.objects.create(
            name="SM FAIRVIEW",
            mobile_no="234234",
            landline_no="234242",
            password="1234"
        )
        
    def test_request_status(self):
        request = HttpRequest()
        response = home(request)
        self.assertEqual(response.status_code, 200)
    
    def test_home_returns_correct_html(self):
        request = HttpRequest()
        response = home(request)
        actual_html = response.content.decode()
        expected_html = render_to_string("queues/home/index.html", { "branches": list(Branch.objects.all().values()) })
        self.assertEqual(actual_html, expected_html)
        
    def test_correct_context(self):
        response = self.client.get("/")
        actual_context = list(response.context)[0]
        expected_context = { "branches": list(Branch.objects.all().values()) }
        self.assertEqual(actual_context, expected_context)


class LoginViewTests(TestCase):
    @classmethod
    def setUpTestData(clf):
        Branch.objects.create(
            name="SM FAIRVIEW",
            mobile_no="234234",
            landline_no="234242",
            password="1234"
        )
    
    def test_password_when_matched(self):
        request = HttpRequest()
        request.POST["branchId"] = 1
        request.POST["password"] = "1234"
        response = login(request)
        actual_data = json.loads(response.content)
        self.assertEqual(actual_data["password_matched"], True)
    
    def test_access_token_when_password_matched(self):
        request = HttpRequest()
        request.POST["branchId"] = 1
        request.POST["password"] = "1234"
        response = login(request)
        actual_data = json.loads(response.content)
        self.assertEqual(actual_data["access_token"], 6)
    
    def test_password_when_not_matched(self):
        request = HttpRequest()
        request.POST["branchId"] = 1
        request.POST["password"] = "1afwef2"
        response = login(request)
        actual_data = json.loads(response.content)
        self.assertEqual(actual_data["password_matched"], False)
    
    def test_access_token_when_password_not_matched(self):
        request = HttpRequest()
        request.POST["branchId"] = 1
        request.POST["password"] = "12adff234"
        response = login(request)
        actual_data = json.loads(response.content)
        self.assertEqual(actual_data["access_token"], None)
        
        

