# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0002_clientinfo_is_usable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientinfo',
            name='room_number',
            field=models.CharField(unique=True, max_length=100),
        ),
    ]
