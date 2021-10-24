import site
from typing import Any, Iterable, List, Optional

from django.apps import AppConfig, apps
from django.contrib.admin.sites import all_sites
from django.core.checks import CheckMessage, Error

from . import get_ignored


def check_admin(
    app_configs: Optional[Iterable[AppConfig]], **kwargs: Any
) -> List[CheckMessage]:
    errors = []
    ignored = get_ignored()
    if not apps.is_installed("django.contrib.admin"):
        errors.append(
            Error(
                "The Django admin app must be in INSTALLED_APPS to use "
                "django-check-admin.",
                hint="Add 'django.contrib.admin' to INSTALLED_APPS.",
            )
        )
        return errors

    if app_configs is None:
        app_configs = apps.get_app_configs()

    registered_models = set()
    for admin_site in all_sites:
        for model, admin in admin_site._registry.items():
            registered_models.add(model)
            for inline in admin.inlines:
                registered_models.add(inline.model)

    errors = []
    for app_config in app_configs:
        # Would use site.getsitepackages(), but can't due to virtualenv bug:
        # https://github.com/pypa/virtualenv/issues/355
        local = not any(app_config.path.startswith(path) for path in site.PREFIXES)
        if local:
            for model in app_config.get_models():
                if model not in ignored:
                    if model not in registered_models:
                        errors.append(
                            Error(
                                "The model %s is not registered with an admin site."
                                % model._meta.label,
                                hint="Register the model in %s.admin or ignore "
                                "this error by adding either checkadmin.ignore() or "
                                "the CHECK_ADMIN_IGNORED_MODELS settings."
                                % app_config.name,
                                obj=model,
                            )
                        )
    return errors
