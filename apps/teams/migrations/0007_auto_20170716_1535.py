# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-16 15:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0006_remove_team_competition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stadium',
            name='capacity',
            field=models.IntegerField(default=''),
        ),
    ]
