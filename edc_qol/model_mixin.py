from django.db import models

from .choices import (
    ANXIETY_DEPRESSION,
    MOBILITY,
    PAIN_DISCOMFORT,
    SELF_CARE,
    USUAL_ACTIVITIES,
)


class Eq5d3lModelMixin(models.Model):
    mobility = models.CharField(verbose_name="Mobility", max_length=45, choices=MOBILITY)

    self_care = models.CharField(verbose_name="SELF-CARE", max_length=45, choices=SELF_CARE)

    usual_activities = models.CharField(
        verbose_name="USUAL ACTIVITIES",
        max_length=45,
        help_text="Example. work, study, housework, family or leisure activities",
        choices=USUAL_ACTIVITIES,
    )

    pain_discomfort = models.CharField(
        verbose_name="PAIN/DISCOMFORT", max_length=45, choices=PAIN_DISCOMFORT
    )

    anxiety_depression = models.CharField(
        verbose_name="ANXIETY / DEPRESSION", max_length=45, choices=ANXIETY_DEPRESSION
    )

    class Meta:
        abstract = True
        verbose_name = "EuroQol EQ-5D-3L Instrument"
        verbose_name_plural = "EuroQol EQ-5D-3L Instrument"
