# Generated by Django 3.2.16 on 2023-02-02 11:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20230202_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='number_of_guests',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
