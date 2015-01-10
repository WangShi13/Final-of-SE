# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0006_signup_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activities',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('describe', models.CharField(max_length=300, null=True)),
                ('author', models.CharField(max_length=30, null=True)),
                ('status', models.CharField(max_length=30)),
                ('create_time', models.DateField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='JoinMe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fullname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50, null=True)),
                ('myclass', models.CharField(max_length=50)),
                ('project', models.CharField(max_length=50)),
                ('describe', models.CharField(max_length=300, null=True)),
                ('status', models.CharField(max_length=50, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fullname', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('describe', models.CharField(max_length=300)),
                ('myactivities', models.ForeignKey(to='mysite.JoinMe')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Signup',
        ),
    ]
