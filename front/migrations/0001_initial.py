# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-11 17:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cover',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.CharField(max_length=100)),
                ('pic', models.CharField(max_length=500)),
            ],
        ),
    ]
