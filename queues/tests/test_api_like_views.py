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