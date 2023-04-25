from django.db import models
from edc_identifier.model_mixins import UniqueSubjectIdentifierFieldMixin
from edc_model.models import BaseUuidModel, HistoricalRecords
from edc_sites.model_mixins import CurrentSiteManager, SiteModelMixin
from edc_utils import get_utcnow

from edc_qol.choices import (
    ICECAP_ACHIEVMENT,
    ICECAP_ATTACHMENT,
    ICECAP_AUTONOMY,
    ICECAP_ENJOYMENT,
    ICECAP_STABILITY,
)


class IcecapaModelMixin(models.Model):
    """
    Al-Janabi H, Flynn TN, Coast J. Development of a self-report
    measure of capability wellbeing for adults: the ICECAP-A.
    Quality of Life Research. 2012;21:167–176
    """

    stability = models.CharField(
        verbose_name="Feeling settled and secure",
        choices=ICECAP_STABILITY,
        max_length=5,
    )

    attachment = models.CharField(
        verbose_name="Love, friendship and support",
        choices=ICECAP_ATTACHMENT,
        max_length=5,
    )

    autonomy = models.CharField(
        verbose_name="Being independent",
        choices=ICECAP_AUTONOMY,
        max_length=5,
    )

    achievement = models.CharField(
        verbose_name="Achievement and progress",
        choices=ICECAP_ACHIEVMENT,
        max_length=5,
    )

    enjoyment = models.CharField(
        verbose_name="Enjoyment and pleasure",
        choices=ICECAP_ENJOYMENT,
        max_length=5,
    )

    class Meta:
        verbose_name = "Overall quality of life (ICECAP-A V2)"
        verbose_name_plural = "Overall quality of life (ICECAP-A V2)"
        abstract = True


class Icecapa(
    UniqueSubjectIdentifierFieldMixin,
    IcecapaModelMixin,
    SiteModelMixin,
    BaseUuidModel,
):
    report_datetime = models.DateTimeField(default=get_utcnow)

    on_site = CurrentSiteManager()
    objects = models.Manager()
    history = HistoricalRecords()

    class Meta(IcecapaModelMixin.Meta, BaseUuidModel.Meta):
        pass
