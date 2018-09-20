# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trade', '0001_initial'),
        ('second_car', '0002_cardetail_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderinfo',
            name='add',
            field=models.ForeignKey(verbose_name='收货地址', to='user.UserAddress'),
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='user',
            field=models.ForeignKey(verbose_name='所属用户', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ordercar',
            name='car_id',
            field=models.ForeignKey(verbose_name='二手车编号', to='second_car.CarDetail'),
        ),
        migrations.AddField(
            model_name='ordercar',
            name='oder',
            field=models.ForeignKey(verbose_name='订单', to='trade.OrderInfo'),
        ),
    ]
