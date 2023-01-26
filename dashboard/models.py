from django.db import models

class Dashboard(models.Model):
    url = models.URLField()
    last_status = models.IntegerField(default=200)
    last_checked = models.DateTimeField()
    last_alert = models.DateTimeField(null=True, blank=True)
