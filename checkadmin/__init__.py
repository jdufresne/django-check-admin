import django

ignored = set()


def ignore(model):
    ignored.add(model)


if django.VERSION < (3, 2):
    default_app_config = "checkadmin.apps.CheckAdminConfig"
