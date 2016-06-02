from django.db import models
from places.models import Place


class Bomber(models.Model):
    macr_nr = models.CharField(max_length=50, blank=True, verbose_name="MARC-Nr")
    air_force = models.CharField(max_length=50, blank=True, verbose_name="Air Force")
    plane_type = models.CharField(max_length=50, blank=True, verbose_name="Type of the aircraft")
    plane_id = models.CharField(max_length=50, blank=True, verbose_name="The aircraft´s ID")
    name = models.CharField(max_length=250, blank=True, verbose_name="Name of the aircraft")
    bomber_group = models.CharField(max_length=50, blank=True, verbose_name="Bomber Group")
    squadron = models.CharField(max_length=75, blank=True)
    date_of_crash = models.DateField(blank=True, null=True)
    reason_of_crash = models.CharField(max_length=250, blank=True)
    target_place = models.ForeignKey(Place, blank=True, null=True, related_name="targetPlace")
    last_seen = models.ForeignKey(Place, blank=True, null=True, related_name="lastSeen")
    crash_place = models.ForeignKey(Place, blank=True, null=True, related_name="crashPlace")
    lat = models.DecimalField(max_digits=20, decimal_places=12, blank=True, null=True)
    lng = models.DecimalField(max_digits=20, decimal_places=12, blank=True, null=True)
    comment = models.TextField(blank=True)

    def __str__(self):
        return "{}".format(self.macr_nr)
