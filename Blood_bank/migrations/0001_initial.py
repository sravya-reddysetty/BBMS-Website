# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-10 15:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_id', models.CharField(max_length=100)),
                ('balance', models.PositiveIntegerField(default=0)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_no', models.CharField(max_length=15)),
                ('locality', models.CharField(max_length=200)),
                ('bank_id', models.CharField(max_length=100)),
                ('blood_group', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Receiver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_no', models.CharField(max_length=15)),
                ('locality', models.CharField(max_length=200)),
                ('bank_id', models.CharField(max_length=100)),
                ('blood_group', models.CharField(max_length=10)),
            ],
        ),
    ]
