# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 11, 21, 17, 30, 21, 40598, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clinictime',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 11, 21, 17, 30, 26, 161722, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
