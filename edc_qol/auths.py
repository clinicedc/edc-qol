from edc_auth.site_auths import site_auths

from .auth_objects import EURO_QOL, EURO_QOL_SUPER, EURO_QOL_VIEW, euro_qol_codenames

site_auths.add_group(*euro_qol_codenames, name=EURO_QOL_VIEW, view_only=True)
site_auths.add_group(*euro_qol_codenames, name=EURO_QOL, no_delete=True)
site_auths.add_group(*euro_qol_codenames, name=EURO_QOL_SUPER)
