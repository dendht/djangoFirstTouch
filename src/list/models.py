from django.db import models
import datetime
from django.contrib.auth.models import User


class Attachment(models.Model):
    # insp = models.ForeignKey
    contributor = models.ForeignKey(User, related_name='+')
    date = models.DateTimeField()
    title = models.CharField(max_length=50)
    attachment = models.FileField()