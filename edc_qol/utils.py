from django.apps import apps as django_apps
from django.conf import settings
from django.db import models

# don't delete. so attr is searchable
EDC_QOL_MODEL = "EDC_QOL_MODEL"


def get_euro_qol_model_name() -> str:
    return getattr(settings, EDC_QOL_MODEL, "edc_qol.mnsi")


def get_euro_qol_model_cls() -> models.Model:
    return django_apps.get_model(getattr(settings, EDC_QOL_MODEL, "edc_qol.mnsi"))
