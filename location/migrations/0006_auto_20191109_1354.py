# Generated by Django 2.2.6 on 2019-11-09 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0005_remove_apartment_estimated_rent_price_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='estimated_rent_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='last_estimated',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='suite_num',
            field=models.CharField(blank=True, max_length=30, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='zillow_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='zpid',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]
