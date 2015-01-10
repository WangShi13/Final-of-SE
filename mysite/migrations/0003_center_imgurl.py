# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_center_urlbutton'),
    ]

    operations = [
        migrations.AddField(
            model_name='center',
            name='imgurl',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
    ]
