# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='number',
            field=models.CharField(default=123, max_length=20),
            preserve_default=False,
        ),
    ]
