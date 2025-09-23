from .utils import (
    get_qol_eq5d3l_model_name,
    get_qol_icecapa_model_name,
    get_qol_sf12_model_name,
)

QOL = "QOL"
QOL_VIEW = "QOL_VIEW"
QOL_SUPER = "QOL_SUPER"

edc_qol_codenames = []


for model in [
    get_qol_eq5d3l_model_name(),
    get_qol_sf12_model_name(),
    get_qol_icecapa_model_name(),
]:
    app_name, model_name = model.split(".")
    for prefix in ["add", "change", "view", "delete"]:
        edc_qol_codenames.append(f"{app_name}.{prefix}_{model_name}")
    edc_qol_codenames.append(f"{app_name}.view_historical{model_name}")
edc_qol_codenames.sort()
