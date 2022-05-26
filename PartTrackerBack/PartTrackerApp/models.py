import datetime
import django.core.validators as validators
from django.db import models
from django.utils import timezone

# Create your models here.
class Filter_Tasks(models.Model):
  part_name         = models.CharField(max_length=20, unique=True)
  quantity          = models.IntegerField(default=0, validators=[validators.MinValueValidator(0)])
  status            = models.IntegerField(default=0)
  date_updated      = models.DateTimeField(default=timezone.now)
  date_due          = models.DateTimeField(null=True, default=None)

class Parts_List_Range(models.Model):
  lower = models.IntegerField(default=0)
  upper = models.IntegerField(default=20)
