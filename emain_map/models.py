"""
Models
"""
from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    """
    One search project.
    """
    name = models.CharField(max_length=255, verbose_name="Short name to display")
    description = models.TextField("Textual description of the search/rescue project")
    commanders = models.ManyToManyField(User, verbose_name="Who is in charge of this", related_name="commanding")
    volunteers = models.ManyToManyField(User, verbose_name="People who are searching", related_name="participating_in")

class Location(models.Model):
    """One location point from one user"""
    project = models.ForeignKey(Project)
    when = models.DateTimeField()
    lat = models.FloatField()
    lon = models.FloatField()
    user = models.ForeignKey(User)

class Message(models.Model):
    """A message from the CC that has to go out to all users"""
    when = models.DateTimeField("When the message was 'sent out'")
    text = models.TextField("Text of the message (HTML)")
    # TODO project
    from_user = models.ForeignKey(User, verbose_name="Who sent this message")


