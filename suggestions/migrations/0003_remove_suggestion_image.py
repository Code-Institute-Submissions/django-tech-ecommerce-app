# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-05-16 09:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suggestions', '0002_suggestion_upvotes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='suggestion',
            name='image',
        ),
    ]