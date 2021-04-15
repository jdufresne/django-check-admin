import django
from django.db import models

ignored = set()


def ignore(model: models.Model) -> None:
    ignored.add(model)


if django.VERSION < (3, 2):
    default_app_config = "checkadmin.apps.CheckAdminConfig"
