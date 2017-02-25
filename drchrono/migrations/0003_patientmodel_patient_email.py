# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drchrono', '0002_auto_20170224_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientmodel',
            name='patient_email',
            field=models.EmailField(default=b'', max_length=254),
        ),
    ]
