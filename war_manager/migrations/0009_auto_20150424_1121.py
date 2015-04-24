# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('war_manager', '0008_auto_20150424_1115'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-date_received']},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-imp_date']},
        ),
    ]
