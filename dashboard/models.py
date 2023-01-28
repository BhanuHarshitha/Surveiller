from django.db import models
from django.contrib.auth.models import User

class Dashboard(models.Model):
    url = models.URLField()
    status = models.IntegerField(default=200)
    status_send_to = models.TextField(default=200)
    last_alert = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, default=None, null=True, on_delete=models.CASCADE)
