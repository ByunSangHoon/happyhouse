# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0003_auto_20150517_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientinfo',
            name='birth',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='clientinfo',
            name='check_in_time',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='clientinfo',
            name='job',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='clientinfo',
            name='nationality',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='clientinfo',
            name='ph_number',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
