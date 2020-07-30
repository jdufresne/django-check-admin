from django.contrib import admin

import checkadmin

from . import models

# Registered models don't emit an error.
admin.site.register(models.MyModel)


# Inlines don't emit an error.
class ChildInline(admin.TabularInline):
    model = models.ChildModel


# Models registered with a decorator don't emit an error.
@admin.register(models.ParentModel)
class MyModel1Admin(admin.ModelAdmin):
    inlines = [ChildInline]


# Ignored models don't emit an error.
checkadmin.ignore(models.IgnoredModel)
