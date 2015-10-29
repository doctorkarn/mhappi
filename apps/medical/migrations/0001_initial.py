# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authenication', '0002_officer_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalRecord',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('symptom', models.TextField()),
                ('diagnosis', models.TextField()),
                ('drg_code', models.CharField(max_length=20)),
                ('officer', models.ForeignKey(to='authenication.Officer')),
                ('patient', models.ForeignKey(to='authenication.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='PatientInfo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('information', models.TextField()),
                ('officer', models.ForeignKey(to='authenication.Officer')),
                ('patient', models.ForeignKey(to='authenication.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='Prescritpion',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('drug_list', models.TextField()),
                ('officer', models.ForeignKey(to='authenication.Officer')),
                ('patient', models.ForeignKey(to='authenication.Patient')),
            ],
        ),
    ]
