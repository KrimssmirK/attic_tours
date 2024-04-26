from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from queues.views.views_home import home, login
from queues.views.views_report import report, api_send_report
from queues.models import Branch, Service
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
        expected_html = render_to_string("queues/home/index.html", { "branches": Branch.get_branch_without_password() })
        self.assertEqual(actual_html, expected_html)
        
    def test_correct_context(self):
        response = self.client.get("/")
        actual_context = list(response.context)[0]
        expected_context = { "branches": Branch.get_branch_without_password() }
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
        branchId = Branch.objects.all().last().id
        request.POST["branchId"] = branchId
        request.POST["password"] = "1234"
        response = login(request)
        actual_data = json.loads(response.content)
        self.assertEqual(actual_data["password_matched"], True)
    
    def test_access_token_when_password_matched(self):
        request = HttpRequest()
        branchId = Branch.objects.all().last().id
        request.POST["branchId"] = branchId
        request.POST["password"] = "1234"
        response = login(request)
        actual_data = json.loads(response.content)
        self.assertEqual(actual_data["access_token"], branchId * 2 + 4)
    
    def test_password_when_not_matched(self):
        request = HttpRequest()
        branchId = Branch.objects.all().last().id
        request.POST["branchId"] = branchId
        request.POST["password"] = "1afwef2"
        response = login(request)
        actual_data = json.loads(response.content)
        self.assertEqual(actual_data["password_matched"], False)
    
    def test_access_token_when_password_not_matched(self):
        request = HttpRequest()
        branchId = Branch.objects.all().last().id
        request.POST["branchId"] = branchId
        request.POST["password"] = "12adff234"
        response = login(request)
        actual_data = json.loads(response.content)
        self.assertEqual(actual_data["access_token"], None)
        

class ReportViewTests(TestCase):
    @classmethod
    def setUpTestData(clf):
        Service.objects.create(
            name="NEW VISA"
        )
        Branch.objects.create(
            name="SM FAIRVIEW",
            mobile_no="234234",
            landline_no="234242",
            password="1234"
        )
    def test_simple_request(self):   
        request = HttpRequest()
        branch = Branch.objects.all().last()
        response = report(request, branch.id)
        self.assertEqual(response.status_code, 200)
    
    def test_send_request_for_report_form(self):
        request = HttpRequest()
        request.POST["service_id"] = Service.objects.all().last().id
        request.POST["pax"] = 3
        request.POST["by"] = "kenji"
        request.POST["branch_id"] = Branch.objects.all().last().id
        response = api_send_report(request)
        actual_data = json.loads(response.content)
        self.assertEqual(actual_data, {})
    
    def test_check_status_after_send_request_to_api_send_report(self):
        request = HttpRequest()
        request.POST["service_id"] = Service.objects.all().last().id
        request.POST["pax"] = 3
        request.POST["by"] = "kenji"
        request.POST["branch_id"] = Branch.objects.all().last().id
        response = api_send_report(request)
        self.assertEqual(response.status_code, 200)
        
    
        

