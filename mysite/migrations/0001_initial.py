# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Center',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('authors', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=30)),
                ('allContent', models.CharField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('authors', models.CharField(max_length=100)),
                ('allContent', models.CharField(max_length=1000)),
                ('publication_date', models.DateField(null=True, blank=True)),
                ('status', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('authors', models.CharField(max_length=100)),
                ('allContent', models.CharField(max_length=1000)),
                ('publication_date', models.DateField(null=True, blank=True)),
                ('status', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fullname', models.CharField(max_length=30)),
                ('myclass', models.CharField(max_length=30)),
                ('num', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=100, verbose_name=b'email', blank=True)),
                ('phonenum', models.CharField(max_length=30)),
                ('dorm', models.CharField(max_length=30)),
                ('describe', models.CharField(max_length=400)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
