from edc_model_admin.admin_site import EdcAdminSite

from .apps import AppConfig

edc_qol_admin = EdcAdminSite(name="edc_qol_admin", app_label=AppConfig.name)
