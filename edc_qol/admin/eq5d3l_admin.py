from django.contrib import admin
from edc_model_admin.dashboard import ModelAdminSubjectDashboardMixin
from edc_model_admin.history import SimpleHistoryAdmin

from ..admin_site import edc_qol_admin
from ..forms import Eq5d3lForm
from ..modeladmin_mixins import Eq5d3lModelAdminMixin
from ..models import Eq5d3l


@admin.register(Eq5d3l, site=edc_qol_admin)
class Eq5d3lAdmin(Eq5d3lModelAdminMixin, ModelAdminSubjectDashboardMixin, SimpleHistoryAdmin):
    form = Eq5d3lForm
