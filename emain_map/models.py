"""
Models
"""
from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    """
    One search project.
    """
    name = models.CharField(max_length=255, verbose_name="Short name to display", null=True)
    description = models.TextField("Textual description of the search/rescue project", null=True)
    commanders = models.ManyToManyField(User, verbose_name="Who is in charge of this", related_name="commanding", null=True)
    volunteers = models.ManyToManyField(User, verbose_name="People who are searching", related_name="participating_in", null=True)

class Location(models.Model):
    """One location point from one user"""
    project = models.ForeignKey(Project, null=True, default=None, blank=True)
    when = models.DateTimeField()
    lat = models.FloatField()
    lon = models.FloatField()
    user = models.ForeignKey(User)

class Message(models.Model):
    """A message from the CC that has to go out to all users"""
    when = models.DateTimeField("When the message was 'sent out'", null=True)
    text = models.TextField("Text of the message (HTML)", null=True)
    project = models.ForeignKey(Project, null=True)
    from_user = models.ForeignKey(User, verbose_name="Who sent this message", null=True)


