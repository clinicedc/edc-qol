from django.test import TestCase

from ...models import Eq5d3l
from .mixins import TestCaseMixin


class TestEq5d3lModel(TestCaseMixin, TestCase):
    def test_pass(self):
        self.assertTrue(True)

    def test_expected_to_fail(self):
        self.assertTrue(False)
