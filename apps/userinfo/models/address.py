from apps.indicators.models.flag import Flag
from django.db import models

from apps.userinfo.models.person import Person

class Address(models.Model):
    street = models.CharField(max_length=30)
    neighborhood = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    cep = models.CharField(max_length=8)
    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE
    )
    status = models.ForeignKey(
        Flag,
        on_delete=models.CASCADE
    )
    creation_dt = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=True) 