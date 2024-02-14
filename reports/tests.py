from django.test import TestCase
from .models import VisaType


class VisaTypeModelTests(TestCase):
    def test_add_visa_type(self):
        """
        add visa type and check if it is added correctly
        """
        new_visa_type = VisaType(visa_type="TOURISM")
        new_visa_type.save()
        visa_type_on_db = VisaType.objects.first()
        self.assertEqual(visa_type_on_db, new_visa_type)
        
