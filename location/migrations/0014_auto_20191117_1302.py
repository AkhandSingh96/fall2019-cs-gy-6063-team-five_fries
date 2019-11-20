# Generated by Django 2.2.7 on 2019-11-17 18:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0013_auto_20191116_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='number_of_bed',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Number of Beds'),
        ),
    ]
