# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='officer',
            name='specialist',
            field=models.ForeignKey(to='authentication.Department', default=0),
        ),
    ]
