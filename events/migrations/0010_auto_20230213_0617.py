# Generated by Django 3.2.17 on 2023-02-13 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_event_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='interested',
        ),
        migrations.RemoveField(
            model_name='event',
            name='slug',
        ),
    ]
