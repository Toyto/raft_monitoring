from django.db import models
from model_utils.models import TimeStampedModel


class ServerLog(TimeStampedModel, models.Model):
    address = models.CharField(max_length=30)
    port = models.CharField(max_length=30)
    read_amount = models.IntegerField(default=0)
    write_amount = models.IntegerField(default=0)
    active = models.BooleanField(default=False)
