from django.db import models
from cardviewer.models import Card
from django.contrib.auth.models import User

# Create your models here.
class Collection(models.Model):
    cards = models.ManyToManyField(Card)
    owner = models.ForeignKey(User)
    def __unicode__(self):
        return owner+ "'s Collection"