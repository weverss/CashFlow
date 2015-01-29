# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_remove_client_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=12, choices=[(b'home', b'Residencial'), (b'work', b'Trabalho'), (b'cellphone', b'Celular')])),
                ('client', models.ForeignKey(to='clients.Client')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
