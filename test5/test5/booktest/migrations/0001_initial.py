# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreaInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('atitle', models.CharField(verbose_name='标题', max_length=20)),
                ('aParent', models.ForeignKey(blank=True, null=True, to='booktest.AreaInfo')),
            ],
        ),
    ]
