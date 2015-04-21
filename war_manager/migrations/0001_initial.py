# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('cid', models.AutoField(serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('mob_number', models.CharField(max_length=24, blank=True)),
                ('region', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'customer',
                'verbose_name_plural': 'customers',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Importer',
            fields=[
                ('iid', models.AutoField(serialize=False, primary_key=True)),
                ('identity', models.CharField(max_length=30, blank=True)),
                ('user_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('msg_text', models.CharField(max_length=511)),
                ('date_received', models.DateField(null=True, blank=True)),
                ('mob_number', models.CharField(max_length=24, blank=True)),
                ('customer', models.ForeignKey(to='war_manager.Customer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('pid', models.AutoField(serialize=False, primary_key=True)),
                ('ser_num', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductImport',
            fields=[
                ('pid', models.AutoField(serialize=False, primary_key=True)),
                ('imp_date', models.DateField(null=True, blank=True)),
                ('importer', models.ForeignKey(to='war_manager.Importer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('mid', models.AutoField(serialize=False, primary_key=True)),
                ('model', models.CharField(max_length=20, blank=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('war_length', models.IntegerField(default=0, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Warranty',
            fields=[
                ('wid', models.AutoField(serialize=False, primary_key=True)),
                ('ser_num', models.CharField(max_length=30, blank=True)),
                ('reg_date', models.DateField(null=True, blank=True)),
                ('exp_date', models.DateField(null=True, blank=True)),
                ('customer', models.ForeignKey(to='war_manager.Customer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='product',
            name='model',
            field=models.ForeignKey(to='war_manager.ProductModel'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='productImport',
            field=models.ForeignKey(to='war_manager.ProductImport'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='warranty',
            field=models.ForeignKey(to='war_manager.Warranty'),
            preserve_default=True,
        ),
    ]
