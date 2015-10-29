# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authenication', '0002_officer_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='officer',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=0),
        ),
        migrations.AddField(
            model_name='patient',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=0),
        ),
        migrations.AlterField(
            model_name='officer',
            name='position',
            field=models.IntegerField(choices=[(1, 'Staff'), (2, 'Doctor'), (3, 'Nurse'), (4, 'Pharmacist')], default=1),
        ),
    ]
