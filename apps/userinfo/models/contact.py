from apps.indicators.models.flag import Flag
from django.db import models

from apps.userinfo.models.person import Person

class Contact(models.Model):
    type = models.ForeignKey(
        Flag,
        on_delete=models.CASCADE,
        related_name="contact_type",
    )
    contact = models.CharField(max_length=100)
    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE
    )
    status = models.ForeignKey(
        Flag,
        on_delete=models.CASCADE,
        related_name="contact_status",
    )
    creation_dt = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=True) 