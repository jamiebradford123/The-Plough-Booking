# Generated by Django 3.2.17 on 2023-02-05 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_alter_book_number_of_guests'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='date',
            field=models.DateField(),
        ),
    ]
