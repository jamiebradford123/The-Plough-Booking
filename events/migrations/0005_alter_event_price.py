# Generated by Django 3.2.17 on 2023-02-05 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20230205_0345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='price',
            field=models.IntegerField(),
        ),
    ]
