from django.core.checks import Error, run_checks
from django.test import TestCase, override_settings

from .models import UnregisteredModel


class CheckAdminTest(TestCase):
    @override_settings(
        INSTALLED_APPS=[
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "django.contrib.sessions",
            "django.contrib.messages",
            "checkadmin",
            "tests",
        ]
    )
    def test_check_dependency(self) -> None:
        errors = run_checks()
        self.assertEqual(
            errors,
            [
                Error(
                    "The Django admin app must be in INSTALLED_APPS to use "
                    "django-check-admin.",
                    hint="Add 'django.contrib.admin' to INSTALLED_APPS.",
                )
            ],
        )

    @override_settings(
        INSTALLED_APPS=[
            "django.contrib.admin",
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "django.contrib.sessions",
            "django.contrib.messages",
            "checkadmin",
            "tests",
        ]
    )
    def test_check_admin(self) -> None:
        errors = run_checks()
        self.assertEqual(
            errors,
            [
                Error(
                    "The model tests.UnregisteredModel is not registered with "
                    "an admin site.",
                    hint="Register the model in tests.admin or ignore this "
                    "error by adding either checkadmin.ignore() or "
                    "the CHECK_ADMIN_IGNORED_MODELS settings.",
                    obj=UnregisteredModel,
                )
            ],
        )

    @override_settings(
        INSTALLED_APPS=[
            "django.contrib.admin",
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "django.contrib.sessions",
            "django.contrib.messages",
            "checkadmin",
            "tests",
        ],
        CHECK_ADMIN_IGNORED_MODELS=[
            "tests.UnregisteredModel",
        ],
    )
    def test_defining_ignored_models_in_settings(self) -> None:
        errors = run_checks()
        self.assertEqual(errors, [])
