# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-21 07:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helloworld', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='showhelloworld',
            name='strn',
            field=models.CharField(default='Hello World', max_length=100),
        ),
        migrations.AlterField(
            model_name='showhelloworld',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
