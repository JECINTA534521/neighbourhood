# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-12-02 05:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neighbour', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='neighbourhood',
            name='health_dpt',
        ),
        migrations.RemoveField(
            model_name='neighbourhood',
            name='health_dpt_address',
        ),
        migrations.RemoveField(
            model_name='neighbourhood',
            name='police',
        ),
        migrations.RemoveField(
            model_name='neighbourhood',
            name='police_dpt_address',
        ),
    ]
