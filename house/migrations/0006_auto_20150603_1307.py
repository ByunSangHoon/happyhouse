# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0005_auto_20150518_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientinfo',
            name='room_type',
            field=models.CharField(max_length=100, null=True, choices=[(b'RT01', b'\xec\x99\xb8\xec\xb0\xbd\xed\x99\x94\xec\x9e\xa5\xec\x8b\xa4'), (b'RT02', b'\xeb\x82\xb4\xec\xb0\xbd\xed\x99\x94\xec\x9e\xa5\xec\x8b\xa4'), (b'RT03', b'\xeb\x82\xb4\xec\xb0\xbd'), (b'RT04', b'\xeb\xac\xb4\xec\xb0\xbd\xed\x99\x94\xec\x9e\xa5\xec\x8b\xa4')]),
        ),
    ]
