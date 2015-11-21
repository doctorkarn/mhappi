# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DrgCode',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='DrugList',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='medicalrecord',
            name='drg_code',
            field=models.ForeignKey(to='medical.DrgCode'),
        ),
    ]
