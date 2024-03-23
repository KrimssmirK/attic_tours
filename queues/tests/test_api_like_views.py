from django.test import TestCase
from django.utils import timezone
from queues.models import Queue, Service


class ApiGetQueueTests(TestCase):

    SERVICES = [
        "Japan Visa", "Korea Visa", "JR Pass", "Wifi", "Package Tour", "Ticket"
    ]

    def setUp(self):
        for SERVICE in self.SERVICES:
            Service.objects.create(name=SERVICE)

    def test_if_the_queue_created(self):
        for SERVICE in self.SERVICES:
            res = self.client.get(f"/queue/api/get_queue/{SERVICE}")
            self.assertEqual(res.status_code, 301)
    
    def test_if_number_change(self):
        for i, _ in enumerate(self.SERVICES):
            res = self.client.get(f"/queue/api/change_number_queue/{i + 1}/1")
            self.assertEqual(res.status_code, 301)
    
    def test_if_window_change(self):
        for i, _ in enumerate(self.SERVICES):
            res = self.client.get(f"/queue/api/change_window_queue/{i + 1}/1")
            self.assertEqual(res.status_code, 301)
    
    def test_if_call_change(self):
        for i, _ in enumerate(self.SERVICES):
            res = self.client.get(f"/queue/api/change_call_queue/{i + 1}/on")
            self.assertEqual(res.status_code, 301)