# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('war_manager', '0007_auto_20150424_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='first_name',
            field=models.CharField(default=b'None', max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customer',
            name='last_name',
            field=models.CharField(default=b'Set', max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='importer',
            field=models.ForeignKey(to='war_manager.Importer', null=True),
            preserve_default=True,
        ),
    ]
