from django.db import models

class Dashboard(models.Model):
    url = models.URLField()
    status = models.IntegerField(default=200)
    status_send_to = models.TextField(default=200)
    last_alert = models.DateTimeField(null=True, blank=True)
