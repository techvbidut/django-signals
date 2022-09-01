from django.db import models

# Reasources used by persons
class Resource(models.Model):
    name = models.CharField(max_length=16)
    description = models.CharField(max_length=32, blank=True)