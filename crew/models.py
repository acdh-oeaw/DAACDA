from django.db import models
from bomber.models import Bomber


class Person(models.Model):
    bomber = models.ForeignKey(Bomber, blank=True, null=True)
    last_name = models.CharField(max_length=250, blank=True)
    first_name = models.CharField(max_length=250, blank=True)
    rank = models.CharField(max_length=250, blank=True)
    service_nr = models.CharField(max_length=250, blank=True)
    destiny_stated = models.CharField(max_length=250, blank=True)
    destiny_checked = models.CharField(max_length=250, blank=True)
    comment = models.TextField(blank=True)
    mia = models.CharField(max_length=250, blank=True)
    position = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return "{}, {}".format(self.last_name, self.first_name)
