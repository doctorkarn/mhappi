# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('symptom', models.TextField()),
                ('diagnosis', models.TextField()),
                ('drg_code', models.CharField(max_length=20)),
                ('officer', models.ForeignKey(to='authentication.Officer')),
                ('patient', models.ForeignKey(to='authentication.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='PatientInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('information', models.TextField()),
                ('officer', models.ForeignKey(to='authentication.Officer')),
                ('patient', models.ForeignKey(to='authentication.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='Prescritpion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('drug_list', models.TextField()),
                ('officer', models.ForeignKey(to='authentication.Officer')),
                ('patient', models.ForeignKey(to='authentication.Patient')),
            ],
        ),
    ]
