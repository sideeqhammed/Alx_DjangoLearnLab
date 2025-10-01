from django.db import models
# from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

# Create your models here.
class Book (models.Model):
  title = models.CharField(max_length=64)
  author = models.CharField(max_length=64)
  published_year = models.PositiveSmallIntegerField(
    validators=[MinValueValidator(1450), MaxValueValidator(datetime.date.today().year)], null=True, blank=True
  )

  def __str__(self):
    return self.title


