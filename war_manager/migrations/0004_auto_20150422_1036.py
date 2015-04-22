# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('war_manager', '0003_auto_20150422_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='customer',
            field=models.ForeignKey(to='war_manager.Customer', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='productImport',
            field=models.ForeignKey(to='war_manager.ProductImport', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='warranty',
            field=models.ForeignKey(to='war_manager.Warranty', null=True),
            preserve_default=True,
        ),
    ]
