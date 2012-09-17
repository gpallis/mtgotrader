from django.db import models

# Create your models here.
class Card(models.Model):
  name = models.CharField(max_length=100)
  picurl = models.CharField(max_length=100)
