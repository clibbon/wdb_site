# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('war_manager', '0004_auto_20150422_1036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='warranty',
            name='ser_num',
        ),
    ]
