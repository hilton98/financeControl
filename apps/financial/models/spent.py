from apps.indicators.models.flag import Flag
from django.db import models

from apps.financial.models.institution import Institution
from apps.userinfo.models.person import Person

class Spent(models.Model):
    value = models.IntegerField()
    description = models.TextField()
    installment = models.IntegerField()
    institution = models.ForeignKey(
        Institution,
        on_delete=models.CASCADE
    )
    status = models.ForeignKey(
        Flag,
        on_delete=models.CASCADE
    )
    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE
    )
    creation_dt = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=True) 