from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class HeartClinicConfig(AppConfig):
    name = 'heart_clinic'
    verbose_name = _('Heart clinic')
