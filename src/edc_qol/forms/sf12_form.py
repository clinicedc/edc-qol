from django import forms
from edc_crf.crf_form_validator import CrfFormValidator
from edc_crf.modelform_mixins import CrfModelFormMixin

from ..models import Sf12


class Sf12FormValidator(CrfFormValidator):
    pass


class Sf12Form(CrfModelFormMixin, forms.ModelForm):
    form_validator_cls = Sf12FormValidator

    class Meta:
        model = Sf12
        fields = "__all__"
