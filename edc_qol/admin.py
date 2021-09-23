from django.contrib import admin

from .admin_site import edc_qol_admin
from .models import Eq5d3l


@admin.register(Eq5d3l, site=edc_qol_admin)
class Eq5d3lAdmin(admin.ModelAdmin):
    pass
