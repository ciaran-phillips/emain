"""
Models
"""
from django.db import models
from django.contrib.auth.models import User


class Location(models.Model):
    when = models.DateTimeField()
    lat = models.FloatField()
    lon = models.FloatField()
    user = models.ForeignKey(User)


