from django.test import TestCase
from django.utils import timezone
from queues.models import Queue, Service


class ModelServiceTests(TestCase):
    def setUp(self):
        self.service = Service(name="Japan Visa")
        self.service.save()
        
    def test_if_the_name_set_properly(self):
        service = Service.objects.get(name="Japan Visa")
        self.assertEqual(service.name, self.service.name)
        
    def test_if_the_display_name_set_properly(self):
        service = Service.objects.get(name="Japan Visa")
        self.assertEqual(str(service), self.service.name)


class ModelQueueTests(TestCase):
    def setUp(self):
        # Setup run before every test method.
        self.service = Service(name="Japan Visa")
        self.service.save()
        Queue(service=self.service).save()
        
    def test_if_the_properties_of_queue_set_properly_for_the_first_time(self):
        queue = Queue.objects.get(service=self.service, date__lte=timezone.now().date())
        self.assertEqual(queue.number, 0)
        self.assertEqual(queue.window, 0)
        self.assertEqual(queue.call, False)
        self.assertEqual(queue.date, timezone.now().date())
        self.assertEqual(queue.service, self.service)
             
    def test_if_the_name_of_queue_set_properly(self):
        queue = Queue.objects.get(service=self.service, date__lte=timezone.now().date())
        self.assertEqual(str(queue), "Japan Visa Queue")
        