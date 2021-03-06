# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-02 17:07
from __future__ import unicode_literals

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0004_team_competition'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='country',
            field=django_countries.fields.CountryField(max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='image',
            field=models.ImageField(blank=True, upload_to='team_image'),
        ),
    ]
