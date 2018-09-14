# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20180914_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='user',
            field=models.ForeignKey(verbose_name='所属的用户', to=settings.AUTH_USER_MODEL),
        ),
    ]
