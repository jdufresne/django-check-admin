from django.apps import AppConfig
from django.core.checks import register

from . import checks


class CheckAdminConfig(AppConfig):
    name = "checkadmin"

    def ready(self) -> None:
        super(CheckAdminConfig, self).ready()
        register(checks.check_admin)
