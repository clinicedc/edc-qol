from django.contrib import admin
from edc_model_admin.dashboard import ModelAdminSubjectDashboardMixin
from edc_model_admin.history import SimpleHistoryAdmin

from ..admin_site import edc_qol_admin
from ..forms import IcecapaForm
from ..modeladmin_mixins import IcecapaModelAdminMixin
from ..models import Icecapa


@admin.register(Icecapa, site=edc_qol_admin)
class IcecapaAdmin(
    IcecapaModelAdminMixin, ModelAdminSubjectDashboardMixin, SimpleHistoryAdmin
):
    form = IcecapaForm
