from django.db import models
from edc_identifier.model_mixins import UniqueSubjectIdentifierFieldMixin
from edc_model.models import BaseUuidModel, HistoricalRecords
from edc_sites.managers import CurrentSiteManager
from edc_sites.model_mixins import SiteModelMixin
from edc_utils import get_utcnow

from ..model_mixins import Eq5d3lModelMixin


class Eq5d3l(
    UniqueSubjectIdentifierFieldMixin,
    Eq5d3lModelMixin,
    SiteModelMixin,
    BaseUuidModel,
):
    report_datetime = models.DateTimeField(default=get_utcnow)

    objects = models.Manager()
    on_site = CurrentSiteManager()
    history = HistoricalRecords()

    class Meta(Eq5d3lModelMixin.Meta, BaseUuidModel.Meta):
        pass
