from edc_auth.site_auths import site_auths

from .auth_objects import QOL, QOL_SUPER, QOL_VIEW, edc_qol_codenames

site_auths.add_group(*edc_qol_codenames, name=QOL_VIEW, view_only=True)
site_auths.add_group(*edc_qol_codenames, name=QOL, no_delete=True)
site_auths.add_group(*edc_qol_codenames, name=QOL_SUPER)
