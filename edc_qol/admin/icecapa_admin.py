from django.contrib import admin
from django_audit_fields import audit_fieldset_tuple
from edc_model_admin.dashboard import ModelAdminSubjectDashboardMixin
from edc_model_admin.history import SimpleHistoryAdmin

from ..admin_site import edc_qol_admin
from ..forms import IcecapaForm
from ..models import Icecapa


def icecapa_fieldsets():
    return [
        (
            "About your overall quality of life",
            {
                "description": (
                    "Please indicate which statements best describe your overall quality "
                    "of life at the moment by selecting ONE option for each of the five "
                    "questions below."
                ),
                "fields": ("stability", "attachment", "autonomy", "achievement", "enjoyment"),
            },
        ),
    ]


def icecapa_radio_fields():
    return {
        "stability": admin.VERTICAL,
        "attachment": admin.VERTICAL,
        "autonomy": admin.VERTICAL,
        "achievement": admin.VERTICAL,
        "enjoyment": admin.VERTICAL,
    }


@admin.register(Icecapa, site=edc_qol_admin)
class IcecapaAdmin(ModelAdminSubjectDashboardMixin, SimpleHistoryAdmin):
    form = IcecapaForm

    fieldsets = (
        (None, {"fields": ("subject_identifier", "report_datetime")}),
        *icecapa_fieldsets(),
        audit_fieldset_tuple,
    )

    radio_fields = icecapa_radio_fields()
