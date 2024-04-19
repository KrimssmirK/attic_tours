from django.test import TestCase
from django.db.utils import IntegrityError
import datetime
from django.utils import timezone
from queues.models import Service, Branch, Report, Window, Queue, Newsfeed, Feedback


class ModelServiceTests(TestCase):
    
    @classmethod
    def setUpTestData(clf):
        """ Run once to set up non-modified data for all class methods """
        
        Service.objects.create(name="Japan Visa", price=1680)
        Service.objects.create(name="JR Pass")
    
    def setUp(self):
        """ Run once for every test method to set up clean data """
        
        Service.objects.create(name="Korea Visa", price=1680)
        pass
    
    def test_name_label(self):
        service = Service.objects.get(id=1)
        field_label = service._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "name")
        
    def test_name_max_length(self):
        service = Service.objects.get(id=1)
        max_length = service._meta.get_field("name").max_length
        self.assertEqual(max_length, 100)
        
    def test_price_default(self):
        service = Service.objects.get(id=1)
        default = service._meta.get_field("price").default
        self.assertEqual(default, 0)
        
    def test_object_name(self):
        service = Service.objects.get(id=1)
        expected_object_name = f"{service.name}"
        self.assertEqual(str(service), expected_object_name)
        
    def test_the_set_name(self):
        service = list(Service.objects.all())[-3]
        self.assertEqual(service.name, "Japan Visa")
        
    def test_the_set_price(self):
        service = Service.objects.all().last()
        self.assertEqual(service.price, 1680)
        
    def test_the_set_price_default(self):
        service = list(Service.objects.all())[-2]
        self.assertEqual(service.price, 0)
        
    def test_change_name(self):
        service = Service.objects.all().last()
        # before the change
        self.assertEqual(service.name, "Korea Visa")
        
        # after the change
        new_service_name = "Visiting Relatives"
        service.name = new_service_name
        self.assertEqual(service.name, new_service_name)
        service.save()
        
        # get the data from the database and verify again
        service = Service.objects.all().last()
        self.assertEqual(service.name, new_service_name)
    
    def test_change_price(self):
        service = Service.objects.all().last()
        # before the change
        self.assertEqual(service.price, 1680)
        
        # after the change
        new_service_price = 1880
        service.price = new_service_price
        self.assertEqual(service.price, new_service_price)
        service.save()
        
        # get the data from the database and verify again
        service = Service.objects.all().last()
        self.assertEqual(service.price, new_service_price)
        
    def test_negative_price_save_fail(self):
        service = Service.objects.all().last()
        with self.assertRaises(IntegrityError):
            service.price = -1
            service.save() 
     
        
class ModelBranchTests(TestCase):
    
    @classmethod
    def setUpTestData(clf):
        Branch.objects.create(
            name="SM MOA",
            mobile_no="0917-631-0848",
            landline_no="(02)8252-0868",
            password="1111"
        )
    
    def setUp(self):
        Branch.objects.create(
            name="SM FAIRVIEW",
            mobile_no="2342142234",
            landline_no="safasfasf32",
            password="0000"
        )
    
    def test_name_label(self):
        branch = Branch.objects.get(id=1)
        field_label = branch._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "name")
    
    def test_name_max_length(self):
        branch = Branch.objects.get(id=1)
        max_length = branch._meta.get_field("name").max_length
        self.assertEqual(max_length, 100)
    
    def test_mobile_no_label(self):
        branch = Branch.objects.get(id=1)
        field_label = branch._meta.get_field("mobile_no").verbose_name
        self.assertEqual(field_label, "mobile no")
        
    def test_mobile_no_max_length(self):
        branch = Branch.objects.get(id=1)
        max_length = branch._meta.get_field("mobile_no").max_length
        self.assertEqual(max_length, 50)
    
    def test_landline_no_label(self):
        branch = Branch.objects.get(id=1)
        field_label = branch._meta.get_field("landline_no").verbose_name
        self.assertEqual(field_label, "landline no")
        
    def test_landline_no_max_length(self):
        branch = Branch.objects.get(id=1)
        max_length = branch._meta.get_field("landline_no").max_length
        self.assertEqual(max_length, 50)
        
    def test_password_label(self):
        branch = Branch.objects.get(id=1)
        field_label = branch._meta.get_field("password").verbose_name
        self.assertEqual(field_label, "password")    
    
    def test_password_max_length(self):
        branch = Branch.objects.get(id=1)
        max_length = branch._meta.get_field("password").max_length
        self.assertEqual(max_length, 50)
    
    def test_object_name(self):
        branch = Branch.objects.get(id=1)
        self.assertEqual(str(branch), branch.name)
        
    def test_verbose_name_plural(self):
        branch = Branch.objects.get(id=1)
        plural_name = branch._meta.verbose_name_plural
        self.assertEqual(plural_name, "branches")
        
    def test_set_landline_no(self):
        branch = Branch.objects.all().last()
        self.assertEqual(branch.mobile_no, "2342142234")
        
    def test_change_landline_no(self):
        branch = Branch.objects.all().last()
        new_landline_no = "0916-618-6165"
        branch.landline_no = new_landline_no
        # before save
        self.assertEqual(branch.landline_no, new_landline_no)
        
        branch.save()
        
        # after save
        branch = Branch.objects.all().last()
        self.assertEqual(branch.landline_no, new_landline_no)


class ModelReportTests(TestCase):
    @classmethod
    def setUpTestData(clf):
        service = Service(name="Tourism", price=1680)
        branch = Branch(
            name="SM FAIRVIEW",
            mobile_no="4213412",
            landline_no="(02)2343-4233",
            password="1111"
        )
        service.save()
        branch.save()
        
        Report.objects.create(
            service=service,
            pax=1,
            by="Arviee",
            branch=branch
        )
        
    def setUp(self):
        pass
    
    def test_set_service(self):
        service = Service.objects.all().last()
        report = Report.objects.get(id=1)
        self.assertEqual(report.service, service)
        
    def test_pax(self):
        report = Report.objects.get(id=1)
        self.assertEqual(report.pax, 1)
        
    def test_by_label(self):
        report = Report.objects.get(id=1)
        field_label = report._meta.get_field("by").verbose_name
        self.assertEqual(field_label, "by")
        
    def test_by_max_length(self):
        report = Report.objects.get(id=1)
        max_length = report._meta.get_field("by").max_length
        self.assertEqual(max_length, 100)
        
    def test_set_branch(self):
        branch = Branch.objects.all().last()
        report = Report.objects.get(id=1)
        self.assertEqual(report.branch, branch)
        
    def test_date(self):
        today_date = timezone.datetime.today().date()
        report = Report.objects.get(id=1)
        self.assertEqual(report.date.date(), today_date)
        
    def test_object_name(self):
        report = Report.objects.get(id=1)
        expected_name = f"{report.service} {report.pax}"
        self.assertEqual(str(report), expected_name)
        
    def test_get_today_reports_with_correct_branch(self):
        branch = Branch.objects.all().last()
        reports = Report.get_today_reports(branch)
        self.assertEqual(reports["Tourism"], 1)
    
    def test_get_today_reports_without_correct_branch(self):
        branch = Branch.objects.all().first()
        reports = Report.get_today_reports(branch)
        self.assertEqual(reports, {})

class ModelWindowTests(TestCase):
    @classmethod
    def setUpTestData(clf):
        Window.objects.create(name="WINDOW 1")
    
    def setUp(self):
        Window.objects.create(name="WINDOW 2")
    
    def test_name_label(self):
        window = Window.objects.get(id=1)
        field_label = window._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "name")
    
    def test_name_max_length(self):
        window = Window.objects.get(id=1)
        max_length = window._meta.get_field("name").max_length
        self.assertEqual(max_length, 50)
        
    def test_object_name(self):
        window = Window.objects.get(id=1)
        self.assertEqual(str(window), window.name)
        
    def test_change_name(self):
        window = Window.objects.get(id=2)
        # before
        self.assertEqual(window.name, "WINDOW 2")
        
        new_name = "WINDOW SALES"
        window.name = new_name
        self.assertEqual(window.name, new_name)
        window.save()
        
        # after
        window = Window.objects.get(id=2)
        self.assertEqual(window.name, new_name)
        

class ModelQueueTests(TestCase):
    @classmethod
    def setUpTestData(clf):
        service = Service(name="Tourism", price=1680)
        branch = Branch(
            name="SM FAIRVIEW",
            mobile_no="4213412",
            landline_no="(02)2343-4233",
            password="1111"
        )
        window = Window(name="WINDOW 1")
        service.save()
        branch.save()
        window.save()
        
        Queue.objects.create(
            branch=branch,
            service=service,
            window=window,
        )
    def setUp(self):
        service = Service(name="Visiting Relatives", price=1680)
        branch = Branch(
            name="SM FAIRVIEW",
            mobile_no="4213412",
            landline_no="(02)2343-4233",
            password="1111"
        )
        window = Window(name="WINDOW VISA")
        service.save()
        branch.save()
        window.save()
        
        Queue.objects.create(
            branch=branch,
            service=service,
            window=window,
        )
    
    def test_set_branch(self):
        branch = list(Branch.objects.all())[-2]
        queue = list(Queue.objects.all())[-2]
        self.assertEqual(queue.branch, branch)
    
    def test_set_service(self):
        service = list(Service.objects.all())[-2]
        queue = list(Queue.objects.all())[-2]
        self.assertEqual(queue.service, service)
        
    def test_no_default(self):
        queue = Queue.objects.get(id=1)
        self.assertEqual(queue.no, 0)
    
    def test_set_window(self):
        window = list(Window.objects.all())[-2]
        queue = list(Queue.objects.all())[-2]
        self.assertEqual(queue.window, window)
    
    def test_call_default(self):
        queue = Queue.objects.get(id=1)
        self.assertEqual(queue.call, False)
        
    def test_date_auto(self):
        current_date = timezone.datetime.today().date()
        queue = Queue.objects.get(id=1)
        self.assertEqual(queue.date, current_date)
    
    def test_object_name(self):
        queue = Queue.objects.get(id=1)
        expected_name = f"{queue.branch}-{queue.service}-{queue.no}-{queue.window}"
        self.assertEqual(str(queue), expected_name)
    
    def test_change_no(self):
        queue = Queue.objects.get(id=2)
        new_no = 1
        queue.no = new_no
        queue.save()
        queue = Queue.objects.get(id=2)
        self.assertEqual(queue.no, new_no)
    
    def test_change_window(self):
        queue = Queue.objects.get(id=2)
        new_window = Window(name="TICKETING")
        new_window.save()
        queue.window = new_window
        queue.save()
        queue = Queue.objects.get(id=2)
        self.assertEqual(queue.window, new_window)
        
    def test_change_call(self):
        queue = Queue.objects.get(id=2)
        new_boolean = True
        queue.call = new_boolean
        queue.save()
        queue = Queue.objects.get(id=2)
        self.assertEqual(queue.call, new_boolean)
    
    def test_window_delete(self):
        window = Window.objects.all().last()
        window.delete()
        queue = Queue.objects.all().last()
        self.assertEqual(queue.window, None)


class ModelNewsfeedTests(TestCase):
    @classmethod
    def setUpTestData(clf):
        branch = Branch(
            name="SM FAIRVIEW",
            mobile_no="4213412",
            landline_no="(02)2343-4233",
            password="1111"
        )
        branch.save()
        
        Newsfeed.objects.create(
            text="Please like and share our FB page",
            branch=branch
        )
    
    def test_text_label(self):
        newsfeed = Newsfeed.objects.get(id=1)
        field_label = newsfeed._meta.get_field("text").verbose_name
        self.assertEqual(field_label, "text")
        
    def test_text_max_length(self):
        newsfeed = Newsfeed.objects.get(id=1)
        max_length = newsfeed._meta.get_field("text").max_length
        self.assertEqual(max_length, 200)
    
    def test_set_branch(self):
        branch = Branch.objects.all().last()
        newsfeed = Newsfeed.objects.all().last()
        self.assertEqual(newsfeed.branch, branch)
    
    def test_object_name(self):
        newsfeed = Newsfeed.objects.get(id=1)
        expected_name = newsfeed.text[:10]
        self.assertEqual(str(newsfeed), expected_name)
        

class ModelFeedbackTests(TestCase):
    @classmethod
    def setUpTestData(clf):
        branch = Branch(
            name="SM FAIRVIEW",
            mobile_no="4213412",
            landline_no="(02)2343-4233",
            password="1111"
        )
        branch.save()
        
        Feedback.objects.create(
            title="Good Design",
            description="well done!!!",
            branch=branch
        )
        
    def test_title_label(self):
        feedback = Feedback.objects.get(id=1)
        field_label = feedback._meta.get_field("title").verbose_name
        self.assertEqual(field_label, "title")
    
    def test_title_max_length(self):
        feedback = Feedback.objects.get(id=1)
        max_length = feedback._meta.get_field("title").max_length
        self.assertEqual(max_length, 100)
        
    def test_description_label(self):
        feedback = Feedback.objects.get(id=1)
        field_label = feedback._meta.get_field("description").verbose_name
        self.assertEqual(field_label, "description")
        
    def test_description_max_length(self):
        feedback = Feedback.objects.get(id=1)
        max_length = feedback._meta.get_field("description").max_length
        self.assertEqual(max_length, 500)
    
    def test_set_branch(self):
        branch = Branch.objects.all().last()
        feedback = Feedback.objects.all().last()
        self.assertEqual(feedback.branch, branch)
    
    def test_set_date(self):
        today_date = timezone.datetime.today().date()
        feedback = Feedback.objects.get(id=1)
        self.assertEqual(feedback.date.date(), today_date)
        
    def test_object_name(self):
        feedback = Feedback.objects.get(id=1)
        expected_name = f"{feedback.branch}-{feedback.title}"
        self.assertEqual(str(feedback), expected_name)
        