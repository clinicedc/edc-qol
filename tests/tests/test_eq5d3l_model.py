from django.test import TestCase

from edc_qol.models import Eq5d3l

from .mixins import TestCaseMixin


class TestEq5d3lModel(TestCaseMixin, TestCase):
    def test_pass(self):
        Eq5d3l()
        self.assertTrue(True)
