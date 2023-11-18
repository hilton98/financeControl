from django.db import models

class Institution(models.Model):
    name = models.CharField(max_length=50)
    creation_dt = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=True) 