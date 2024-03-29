# Generated by Django 4.1.5 on 2023-01-28 06:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0005_rename_last_alert_dashboard_last_alert_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dashboard',
            name='user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='last_alert',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
