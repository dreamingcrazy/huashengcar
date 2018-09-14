# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20180914_1353'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('order_id', models.IntegerField(verbose_name='订单号', primary_key=True, serialize=False)),
                ('price', models.DecimalField(verbose_name='交易价：万', max_digits=10, decimal_places=2)),
                ('Service_Charge', models.DecimalField(verbose_name='手续费', max_digits=10, decimal_places=2)),
                ('freight', models.DecimalField(verbose_name='运费', max_digits=10, decimal_places=2)),
                ('status', models.IntegerField(verbose_name='订单状态', default=0, choices=[(0, '未支付'), (1, '已支付'), (2, '未运输'), (3, '运输中'), (4, '交易成功'), (5, '交易关闭')])),
                ('add', models.ForeignKey(verbose_name='收货地址', to='user.UserAddress')),
                ('user', models.ForeignKey(verbose_name='所属用户', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
