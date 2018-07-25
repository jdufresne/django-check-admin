from django.db import models


class MyModel(models.Model):
    name = models.CharField(max_length=100)


class ParentModel(models.Model):
    name = models.CharField(max_length=100)


class ChildModel(models.Model):
    model1 = models.ForeignKey(ParentModel, models.PROTECT)


class IgnoredModel(models.Model):
    name = models.CharField(max_length=100)


class UnregisteredModel(models.Model):
    name = models.CharField(max_length=100)
