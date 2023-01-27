# Generated by Django 4.1.5 on 2023-01-27 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_rename_website_dashboard'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dashboard',
            old_name='last_alert',
            new_name='Last_Alert',
        ),
        migrations.RenameField(
            model_name='dashboard',
            old_name='url',
            new_name='URL',
        ),
        migrations.RemoveField(
            model_name='dashboard',
            name='last_checked',
        ),
        migrations.RemoveField(
            model_name='dashboard',
            name='last_status',
        ),
        migrations.AddField(
            model_name='dashboard',
            name='Status_Send_To',
            field=models.TextField(default=200),
        ),
    ]
