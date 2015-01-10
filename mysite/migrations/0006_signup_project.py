# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0005_project_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='project',
            field=models.CharField(max_length=30, null=True),
            preserve_default=True,
        ),
    ]
