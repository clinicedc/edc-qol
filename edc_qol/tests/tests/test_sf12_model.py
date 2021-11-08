from django.test import TestCase

from edc_qol.models import Sf12

from .mixins import TestCaseMixin


class TestEq5d3lModel(TestCaseMixin, TestCase):
    def test_pass(self):
        Sf12()
        self.assertTrue(True)
