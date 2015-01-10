# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0007_auto_20150107_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='num',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
    ]
