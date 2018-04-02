from django.db import models


class Test(models.Model):
    name = models.CharField('name', max_length=32)
    age = models.SmallIntegerField('age', null=True)
    birth = models.DateField('birthday', blank=True, null=True)
