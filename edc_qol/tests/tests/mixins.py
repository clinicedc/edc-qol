from django.test import TestCase
from edc_utils import get_utcnow


class TestCaseMixin(TestCase):
    def setUp(self):
        self.subject_identifier = "1234"
        self.data = dict(
            subject_identifier=self.subject_identifier, report_datetime=get_utcnow()
        )
