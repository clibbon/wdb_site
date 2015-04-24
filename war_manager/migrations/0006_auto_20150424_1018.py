# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('war_manager', '0005_remove_warranty_ser_num'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimport',
            name='importer',
        ),
        migrations.RemoveField(
            model_name='product',
            name='productImport',
        ),
        migrations.DeleteModel(
            name='ProductImport',
        ),
        migrations.AddField(
            model_name='product',
            name='imp_date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='importer',
            field=models.OneToOneField(null=True, to='war_manager.Importer'),
            preserve_default=True,
        ),
    ]
