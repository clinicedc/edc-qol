from django import forms
from edc_crf.modelform_mixins import CrfModelFormMixin
from edc_form_validators import FormValidator


class IcecapaFormValidator(FormValidator):
    pass


class IcecapaForm(CrfModelFormMixin, forms.ModelForm):
    form_validator_cls = IcecapaFormValidator
