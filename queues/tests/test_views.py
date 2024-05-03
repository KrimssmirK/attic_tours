from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from queues.views.views_home import home, login
from queues.views.views_report import report, api_send_report
from queues.views.views_queue import api_get_services, api_create_pref_queue, api_delete_pref_queue
from queues.models import Branch, Service, PrefQueue
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


class ViewQueueTests(TestCase):

    @classmethod
    def setUpTestData(clf):
        ViewQueueTests.pref_queue = PrefQueue.objects.create(
            branch=Branch.objects.all().first(), 
            service=Service.objects.all().first())
        
    def test_json_correct(self):
        services = Service.objects.all().values()
        request = HttpRequest()
        response = api_get_services(request)
        actual_data = json.loads(response.content) # json string to json object
        self.assertEqual(actual_data["services"], list(services))
    
    def test_the_status_when_add_new_preference_queue_success(self):
        request = HttpRequest()
        request.POST["branch_id"] = 3
        request.POST["service_id"] = 1
        response = api_create_pref_queue(request)
        pref_queue = PrefQueue.objects.all().last()
        data = json.loads(response.content)
        self.assertEqual(data["status"], f"{pref_queue} has been added to preference queue")
    
    def test_the_status_when_add_new_preference_queue_failure(self):
        request = HttpRequest()
        request.POST["branch_id"] = 1
        request.POST["service_id"] = 1
        response = api_create_pref_queue(request)
        data = json.loads(response.content)
        self.assertEqual(data["status"], "has already in preference queue")
    
    def test_the_added_preference_queue_if_the_info_matches(self):
        # constant
        BRANCH_ID = 3
        SERVICE_ID = 6
        # client
        request = HttpRequest()
        request.POST["branch_id"] = BRANCH_ID
        request.POST["service_id"] = SERVICE_ID
        
        # server
        api_create_pref_queue(request)
        
        # db
        pref_queue = PrefQueue.objects.all().last()
        self.assertEqual(pref_queue.branch.id, BRANCH_ID)
        self.assertEqual(pref_queue.service.id, SERVICE_ID)
        
    def test_api_delete_pref_queue_if_deletes(self):
        request = HttpRequest()
        request.POST["pref_queue_id"] = ViewQueueTests.pref_queue.id
        api_delete_pref_queue(request)
        pref_queue = PrefQueue.objects.all()
        self.assertEqual(pref_queue.exists(), False)
        
    def test_api_read_queues_if_the_data_is_correct(self):
        pass