# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('war_manager', '0011_auto_20150427_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='importer',
            field=models.ForeignKey(blank=True, to='war_manager.Importer', null=True),
            preserve_default=True,
        ),
    ]
