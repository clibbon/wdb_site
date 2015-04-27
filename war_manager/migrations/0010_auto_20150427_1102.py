# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('war_manager', '0009_auto_20150424_1121'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-pid']},
        ),
        migrations.AddField(
            model_name='productmodel',
            name='long_name',
            field=models.CharField(max_length=60, null=True),
            preserve_default=True,
        ),
    ]
