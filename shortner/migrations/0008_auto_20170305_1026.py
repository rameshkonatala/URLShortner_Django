# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-05 10:26
from __future__ import unicode_literals

from django.db import migrations, models
import shortner.validators


class Migration(migrations.Migration):

    dependencies = [
        ('shortner', '0007_auto_20170304_0709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kirrurl',
            name='url',
            field=models.CharField(max_length=220, validators=[shortner.validators.validate_url, shortner.validators.validate_dot_com]),
        ),
    ]
