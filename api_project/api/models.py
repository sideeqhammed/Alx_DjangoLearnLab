from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book (models.Model):
  title = models.CharField(max_length=64)
  author = models.CharField(max_length=64)
  published_date = models.DateField(null=True, blank=True)

