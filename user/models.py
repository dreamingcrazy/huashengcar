from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core import validators


class UserInfo(AbstractUser):
    is_delete = models.IntegerField(default=0)
    def __str__(self):
        return self.username
class Meta:
    db_table = 'userinfo'
    verbose_name = '用户信息'
    verbose_name_plural = verbose_name
class UserAddress(models.Model):
    user = models.ForeignKey('UserInfo',null=False,verbose_name='所属的用户')
    recv = models.CharField( max_length=10,null=False,verbose_name='收货人' ,unique=True,
        help_text=('Required. 30 characters or fewer. Letters, digits and '
                    '@/./+/-/_ only.'),
        validators=[
            validators.RegexValidator(r'^[\w.@+-]+$',
                                      ('Enter a valid username. '
                                        'This value may contain only letters, numbers '
                                        'and @/./+/-/_ characters.'), 'invalid'),
        ],
        error_messages={
            'unique': ("A user with that username already exists."),
        })
    recv_phone = models.IntegerField(max_length=11,verbose_name='收货人联系方式'),
    service_phone = models.IntegerField(verbose_name='客服电话'),
    add = models.CharField(max_length=50,verbose_name='收货人地址')
    is_delete = models.BooleanField(default=0,null=False,verbose_name='是否删除')
# Create your models here.
