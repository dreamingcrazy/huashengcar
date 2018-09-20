# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderCar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='更新时间', auto_now_add=True)),
                ('is_delete', models.BooleanField(verbose_name='是否删除', default=False)),
                ('comment', models.CharField(verbose_name='评论', max_length=1000)),
            ],
            options={
                'verbose_name': '订单车辆',
                'verbose_name_plural': '订单车辆',
            },
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='更新时间', auto_now_add=True)),
                ('is_delete', models.BooleanField(verbose_name='是否删除', default=False)),
                ('order_id', models.CharField(verbose_name='订单号', primary_key=True, max_length=50, serialize=False)),
                ('price', models.DecimalField(verbose_name='交易价:万', max_digits=10, decimal_places=2)),
                ('Service_Charge', models.DecimalField(verbose_name='手续费', max_digits=10, decimal_places=2)),
                ('freight', models.DecimalField(verbose_name='运费', max_digits=10, decimal_places=2)),
                ('status', models.IntegerField(verbose_name='订单状态', default=0, choices=[(0, '未支付'), (1, '已支付'), (2, '未运输'), (3, '运输中'), (4, '交易成功'), (5, '交易关闭')])),
                ('pay_method', models.IntegerField(verbose_name='选择交易方式', default=0, choices=[(0, '线上'), (1, '线下')])),
                ('online_pay_method', models.IntegerField(verbose_name='线上支付方式', default=2, choices=[(0, '银联支付'), (1, '微信支付'), (2, '支付宝')])),
            ],
            options={
                'verbose_name': '订单信息',
                'verbose_name_plural': '订单信息',
            },
        ),
    ]
