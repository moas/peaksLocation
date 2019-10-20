# Generated by Django 2.2.6 on 2019-10-20 23:19

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodes', '0002_auto_20191020_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peak',
            name='coordinates',
            field=django.contrib.gis.db.models.fields.PointField(dim=3, srid=4326, unique=True),
        ),
        migrations.AlterField(
            model_name='peak',
            name='slug_name',
            field=models.SlugField(editable=False, max_length=30),
        ),
    ]