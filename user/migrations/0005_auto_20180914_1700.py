# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20180914_1623'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userinfo',
            options={'verbose_name': '用户信息', 'verbose_name_plural': '用户信息'},
        ),
        migrations.AlterModelTable(
            name='userinfo',
            table='userinfo',
        ),
    ]
