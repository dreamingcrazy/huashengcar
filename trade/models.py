from django.db import models
class OrderInfo(models.Model):
    order_status = (
        (0,'未支付'),(1,'已支付'),(2,'未运输'),(3,'运输中'),(4,'交易成功'),(5,'交易关闭')
    )
    pay_way = (
        (0,'线下'),(1,'贷款'),(2,'支付宝'),(3,'微信')
    )
    order_id = models.IntegerField(verbose_name='订单号',primary_key=True)
    user = models.ForeignKey('user.UserInfo',verbose_name='所属用户')
    add = models.ForeignKey('user.UserAddress',verbose_name='收货地址')
    price = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='交易价：万')
    Service_Charge = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='手续费')
    freight = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='运费')
    status = models.IntegerField(choices=order_status,default=0,verbose_name='订单状态')
# Create your models here.
