# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('war_manager', '0002_customer_profile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='warranty',
            options={'verbose_name_plural': 'Warranties'},
        ),
        migrations.AlterField(
            model_name='customer',
            name='profile',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='warranty',
            name='customer',
            field=models.ForeignKey(to='war_manager.Customer', null=True),
            preserve_default=True,
        ),
    ]
