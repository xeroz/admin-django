# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-24 23:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0002_player_player'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='integer',
            new_name='number',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='player',
            new_name='team',
        ),
    ]
