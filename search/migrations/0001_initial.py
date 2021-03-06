# Generated by Django 2.2.6 on 2019-10-25 18:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CraigslistLocation',
            fields=[
                ('c_id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('date_time', models.DateTimeField()),
                ('url', models.URLField()),
                ('price', models.CharField(max_length=200)),
                ('where', models.CharField(max_length=200)),
                ('has_image', models.BooleanField(default=False)),
                ('has_map', models.BooleanField(default=False)),
                ('lat', models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True)),
                ('lon', models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LastRetrievedData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=200, unique=True)),
                ('time', models.DateTimeField(default=datetime.datetime.now, verbose_name='last retrieval')),
            ],
        ),
    ]
