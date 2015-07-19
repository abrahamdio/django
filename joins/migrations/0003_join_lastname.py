# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0002_join_firstname'),
    ]

    operations = [
        migrations.AddField(
            model_name='join',
            name='lastname',
            field=models.CharField(default=b'lastname', max_length=20),
        ),
    ]
