from django.db import models

class Flag(models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField()
    creation_dt = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=True) 