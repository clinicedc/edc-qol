from edc_crf.crf_model_mixin import CrfModelMixin
from edc_model import models as edc_models


class Eq5d3l(
    CrfModelMixin,
    edc_models.BaseUuidModel,
):
    class Eq5d3l(CrfModelMixin.Meta, edc_models.BaseUuidModel.Meta):
        verbose_name = "EuroQol EQ-5D-3L Instrument"
        verbose_name_plural = "EuroQol EQ-5D-3L Instrument"
