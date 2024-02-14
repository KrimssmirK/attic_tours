from django.test import TestCase
from .models import VisaType, Coordinator


class VisaTypeModelTests(TestCase):
    def test_add_visa_type(self):
        """
        add visa type and check if it is added correctly
        """
        new_visa_type = VisaType(visa_type="TOURISM")
        new_visa_type.save()
        visa_type_on_db = VisaType.objects.first()
        self.assertEqual(visa_type_on_db, new_visa_type)
        

class CoordinatorModelTests(TestCase):
    """
    add coordinator and check if it is added correctly
    """
    def test_add_coordinator(self):
        new_coordinator = Coordinator(name="arvie")
        new_coordinator.save()
        coordinator_on_db = Coordinator.objects.first()
        self.assertEqual(coordinator_on_db, new_coordinator)