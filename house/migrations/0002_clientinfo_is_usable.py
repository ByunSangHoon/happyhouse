# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientinfo',
            name='is_usable',
            field=models.BooleanField(default=False),
        ),
    ]
