# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PatientModel',
            fields=[
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('doctor_id', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('birthday', models.CharField(max_length=10)),
                ('patient_id', models.IntegerField(serialize=False, primary_key=True)),
            ],
        ),
    ]
