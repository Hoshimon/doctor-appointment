# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-26 01:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0005_auto_20170626_0120'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='specialty',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
    ]