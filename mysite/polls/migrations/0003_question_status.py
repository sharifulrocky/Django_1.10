# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-23 16:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20161123_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='status',
            field=models.CharField(choices=[(b'd', b'Draft'), (b's', b'Submitted'), (b'c', b'Cancel')], default='d', max_length=50),
            preserve_default=False,
        ),
    ]
