# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0002_auto_20151121_1908'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicalrecord',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 11, 21, 17, 30, 31, 18105, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patientinfo',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 11, 21, 17, 30, 33, 327678, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prescritpion',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 11, 21, 17, 30, 35, 237592, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
