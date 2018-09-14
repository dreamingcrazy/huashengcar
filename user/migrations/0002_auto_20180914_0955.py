# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraddress',
            name='recv_phone',
        ),
        migrations.RemoveField(
            model_name='useraddress',
            name='service_phone',
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='add',
            field=models.CharField(verbose_name='收货人地址', max_length=50),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='is_delete',
            field=models.BooleanField(verbose_name='是否删除', default=0),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='recv',
            field=models.CharField(verbose_name='收货人', max_length=10, unique=True, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], error_messages={'unique': 'A user with that username already exists.'}),
        ),
    ]
