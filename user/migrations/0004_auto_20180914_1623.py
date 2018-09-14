# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20180914_1353'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='true_name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='last_name',
            field=models.CharField(verbose_name='last name', max_length=30, blank=True),
        ),
    ]
