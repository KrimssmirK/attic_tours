from django.test import TestCase
from django.utils import timezone
from .models import VisaType, Coordinator, Report


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
        
    
class ReportModelTests(TestCase):
    def setUp(self):
        """
        set up first the visa type and coordinator
        """
        VisaType.objects.create(visa_type="relatives")
        Coordinator.objects.create(name="arvie")
        
        
    def test_add_report(self):
        """
        add report and check it is added correctly
        """
        visa_type = VisaType.objects.first()
        coordinator = Coordinator.objects.first()
        new_report = Report(visa_type=visa_type, coordinator=coordinator, no_of_pax=2, report_date=timezone.now())
        new_report.save()
        report_on_db = Report.objects.first()
        self.assertEqual(report_on_db, new_report)
        