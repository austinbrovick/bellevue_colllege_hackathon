# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-20 07:24
from __future__ import unicode_literals

import clubs.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='club_picture',
            field=models.ImageField(blank=True, null=True, upload_to=clubs.models.upload_location),
        ),
    ]
