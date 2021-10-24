from typing import Set

import django
from django.apps import apps as django_apps
from django.conf import settings
from django.db import models

ignored = set()


def ignore(model: models.Model) -> None:
    ignored.add(model)


def get_ignored() -> Set[models.Model]:
    ignored_models = getattr(settings, "CHECK_ADMIN_IGNORED_MODELS", [])
    for model_path in ignored_models:
        model = django_apps.get_model(*model_path.rsplit(".", 1), False)
        ignored.add(model)
    return ignored


if django.VERSION < (3, 2):
    default_app_config = "checkadmin.apps.CheckAdminConfig"
