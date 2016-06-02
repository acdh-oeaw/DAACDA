from django.db import models


class Label(models.Model):
    label = models.CharField(max_length=100, blank=True, help_text="The entities label or name.")
    label_type = models.CharField(max_length=255, blank=True, help_text="The type of the label.")
    isoCode = models.CharField(
        max_length=3, blank=True, help_text="The ISO 639-3 code for the label's language."
    )

    def __str__(self):
        return "{}".format(self.label)
