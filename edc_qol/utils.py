from django.apps import apps as django_apps
from django.conf import settings
from django.db import models

# don't delete. so attr is searchable
EDC_QOL_EQ5D3L_MODEL = "EDC_QOL_EQ5D3L_MODEL"
EDC_QOL_SF12_MODEL = "EDC_QOL_SF12_MODEL"
EDC_QOL_ICECAPA_MODEL = "EDC_QOL_ICECAPA_MODEL"


def get_qol_eq5d3l_model_name() -> str:
    return getattr(settings, EDC_QOL_EQ5D3L_MODEL, "edc_qol.eq5d3l")


def get_qol_eq5d3l_model_cls() -> models.Model:
    return django_apps.get_model(get_qol_eq5d3l_model_name())


def get_qol_sf12_model_name() -> str:
    return getattr(settings, EDC_QOL_SF12_MODEL, "edc_qol.sf12")


def get_qol_sf12_model_cls() -> models.Model:
    return django_apps.get_model(get_qol_sf12_model_name())


def get_qol_icecapa_model_name() -> str:
    return getattr(settings, EDC_QOL_ICECAPA_MODEL, "edc_qol.icecapa")


def get_qol_icecapa_model_cls() -> models.Model:
    return django_apps.get_model(get_qol_icecapa_model_name())
