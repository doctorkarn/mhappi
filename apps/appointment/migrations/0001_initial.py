# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('appointment_status', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ClinicTime',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('clinic_datetime', models.DateTimeField()),
                ('clinic_status', models.SmallIntegerField()),
                ('officer', models.ForeignKey(to='authentication.Officer')),
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
            field=models.ForeignKey(to='authentication.Patient'),
        ),
    ]
