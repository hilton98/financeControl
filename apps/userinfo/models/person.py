from apps.indicators.models.flag import Flag
from django.contrib.auth.models import User
from django.db import models

class Person(models.Model):
    full_name = models.CharField(max_length=80)
    name = models.CharField(max_length=15)
    surname = models.CharField(max_length=15)
    born_dt = models.DateTimeField()
    cpf = models.CharField(max_length=11)
    status = models.ForeignKey(
        Flag,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    creation_dt = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=True) 
