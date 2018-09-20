from django.db import models
from db.basemodel import BaseModel

# Create your models here.






class OrderInfo(BaseModel):
    '''订单模型'''
    ORDER_STATUS = (
        (0,'未支付'),(1,'已支付'),(2,'未运输'),(3,'运输中'),(4,'交易成功'),(5,'交易关闭')

    )
    PAY_METHOD = (
        (0,'线上'),
        (1,'线下')
    )
    ONLINE_PAY_METHOD=(
        (0,'银联支付'),(1,'微信支付'),(2,'支付宝')
    )



    order_id = models.CharField(max_length=50,verbose_name='订单号',primary_key=True)
    user = models.ForeignKey('user.UserInfo',verbose_name='所属用户')
    add = models.ForeignKey('user.UserAddress',verbose_name='收货地址')
    price = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='交易价:万')
    Service_Charge = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='手续费')
    freight = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='运费')
    status = models.IntegerField(choices=ORDER_STATUS,default=0,verbose_name='订单状态')
    pay_method = models.IntegerField(choices=PAY_METHOD,default=0,verbose_name='选择交易方式')
    online_pay_method = models.IntegerField(choices=ONLINE_PAY_METHOD,default=2,verbose_name='线上支付方式')


    class Meta:
        verbose_name = '订单信息'
        verbose_name_plural = verbose_name


class OrderCar(BaseModel):
    '''订单车辆'''
    oder = models.ForeignKey('OrderInfo',verbose_name='订单')
    car_id = models.ForeignKey('second_car.CarDetail',verbose_name='二手车编号')
    comment = models.CharField(max_length=1000,verbose_name='评论')


    class Meta:
        verbose_name = '订单车辆'
        verbose_name_plural = verbose_name
