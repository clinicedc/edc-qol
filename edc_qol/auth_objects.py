from django.conf import settings
from django.db import models

EURO_QOL = "EURO_QOL"
EURO_QOL_VIEW = "EURO_QOL_VIEW"
EURO_QOL_SUPER = "EURO_QOL_SUPER"

euro_qol_codenames = []


def get_eq5d3l_model_name() -> models.Model:
    return getattr(settings, "EDC_QOL_EQ5D3L_MODEL", "edc_qol.eq5d3l")


for model in [get_eq5d3l_model_name()]:
    app_name, model_name = model.split(".")
    for prefix in ["add", "change", "view", "delete"]:
        euro_qol_codenames.append(f"{app_name}.{prefix}_{model_name}")
    euro_qol_codenames.append(f"{app_name}.view_historical{model_name}")
euro_qol_codenames.sort()
