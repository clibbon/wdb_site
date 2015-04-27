# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('war_manager', '0010_auto_20150427_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date_received',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
