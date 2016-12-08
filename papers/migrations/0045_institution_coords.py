# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-29 20:41
from __future__ import unicode_literals

from django.db import migrations
import djgeojson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0044_country_and_no_cascading_deletion'),
    ]

    operations = [
        migrations.AddField(
            model_name='institution',
            name='coords',
            field=djgeojson.fields.PointField(blank=True, null=True),
        ),
    ]