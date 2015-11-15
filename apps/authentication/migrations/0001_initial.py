# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Officer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('hospital_id', models.CharField(max_length=20)),
                ('national_id', models.CharField(max_length=20)),
                ('prefix_name', models.CharField(max_length=200)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('gender', models.IntegerField(choices=[(1, 'Male'), (2, 'Female'), (3, 'Others')])),
                ('birthdate', models.DateField()),
                ('address', models.CharField(max_length=500)),
                ('phone', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('specialist', models.CharField(max_length=200)),
                ('position', models.IntegerField(choices=[(1, 'Staff'), (2, 'Doctor'), (3, 'Nurse'), (4, 'Pharmacist')], default=1)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('hospital_id', models.CharField(max_length=20)),
                ('national_id', models.CharField(max_length=20)),
                ('prefix_name', models.CharField(max_length=200)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('gender', models.IntegerField(choices=[(1, 'Male'), (2, 'Female'), (3, 'Others')])),
                ('birthdate', models.DateField()),
                ('address', models.CharField(max_length=500)),
                ('phone', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, default=0)),
            ],
        ),
    ]
