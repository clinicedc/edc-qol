from copy import deepcopy

from django.test import TestCase
from django.utils import timezone

from edc_qol.constants import (
    NO_PAIN_DISCOMFORT,
    NO_PROBLEM_SELF_CARE,
    NO_PROBLEM_USUAL_ACTIVITIES,
    NO_PROBLEM_WALKING,
    NOT_ANXIOUS_DEPRESSED,
)


class TestCaseMixin(TestCase):
    def setUp(self):
        self.subject_identifier = "1234"
        self.data = dict(
            subject_identifier=self.subject_identifier,
            report_datetime=timezone.now,
        )

    def get_best_case_patient_history_data(self):
        data = deepcopy(self.data)
        data.update(
            {
                "anxiety_depression": NOT_ANXIOUS_DEPRESSED,
                "mobility": NO_PROBLEM_WALKING,
                "pain_discomfort": NO_PAIN_DISCOMFORT,
                "self_care": NO_PROBLEM_SELF_CARE,
                "usual_activities": NO_PROBLEM_USUAL_ACTIVITIES,
            }
        )
        return data
