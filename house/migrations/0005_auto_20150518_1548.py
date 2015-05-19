# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0004_auto_20150517_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientinfo',
            name='room_type',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
