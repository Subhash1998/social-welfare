# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-17 07:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0006_question_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='user',
        ),
        migrations.AddField(
            model_name='question',
            name='user_name',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
    ]
