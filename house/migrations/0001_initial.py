# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('room_number', models.CharField(max_length=100)),
                ('resident_name', models.CharField(max_length=100)),
                ('room_type', models.CharField(max_length=4, null=True)),
                ('price', models.PositiveIntegerField()),
                ('real_price', models.PositiveIntegerField()),
                ('etc', models.TextField(null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
