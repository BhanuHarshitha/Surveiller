# Generated by Django 4.1.5 on 2023-01-30 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_dashboard_user_alter_dashboard_last_alert'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboard',
            name='url',
            field=models.TextField(default=200),
        ),
    ]
