# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-06 00:23
from __future__ import unicode_literals

from django.db import migrations, models
import silk.models


class Migration(migrations.Migration):

    dependencies = [
        ('silk', '0003_request_prof_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='prof_file',
            field=models.FileField(null=True, storage=silk.models.silk_storage, upload_to=''),
        ),
    ]
