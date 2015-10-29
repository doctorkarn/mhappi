# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authenication', '0002_officer_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('appointment_status', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ClinicTime',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('clinic_datetime', models.DateTimeField()),
                ('clinic_status', models.SmallIntegerField()),
                ('officer', models.ForeignKey(to='authenication.Officer')),
            ],
        ),
        migrations.AddField(
            model_name='appointment',
            name='clinic_time',
            field=models.ForeignKey(to='appointment.ClinicTime'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='patient',
            field=models.ForeignKey(to='authenication.Patient'),
        ),
    ]
