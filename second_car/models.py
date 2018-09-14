from django.db import models
class CarStyle(models.Model):
    name = models.CharField(max_length=10,verbose_name='车辆类型')
    image = models.ImageField(upload_to='type',verbose_name='车辆代表性图片')
    class Meta:
        verbose_name = '车辆类型'
        verbose_name_plural = verbose_name
class Brande(models.Model):
    name = models.CharField(max_length=10,verbose_name='车辆品牌')
    class Meta:
        verbose_name = '车辆品牌'
        verbose_name_plural = verbose_name
class CarDetail(models.Model):
    status_choice = (
        (0,'下线'),
        (1,'上线')
    )
    user = models.ForeignKey('user.UserInfo',verbose_name='所属用户')
    style = models.ForeignKey('CarStyle',verbose_name='所属类型')
    brande = models.ForeignKey('Brande',verbose_name='所属品牌')
    car_model = models.CharField(max_length=5,verbose_name='车型')
    color = models.CharField(max_length=5,verbose_name='颜色')
    age = models.CharField(max_length=10,verbose_name='车龄')
    transmission_case = models.CharField(max_length=10,verbose_name='变速箱')
    mileage = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='里程数')
    displacement = models.CharField(max_length=10,verbose_name='排量')
    emission_standard = models.CharField(max_length=10, verbose_name='排放标准')
    Fuel_type = models.CharField(max_length=10,verbose_name='燃油类型')
    License_plate_location = models.CharField(max_length=10,verbose_name='车牌所在地')
    drive = models.CharField(max_length=10,verbose_name='驱动')
    country = models.CharField(max_length=10,verbose_name='国别')
    status = models.IntegerField(default=1,choices=status_choice,verbose_name='状态')
    class Meta:
        verbose_name = '车辆细节'
        verbose_name_plural = verbose_name
class Image_detail(models.Model):
    path = models.ImageField(upload_to='/detail_img',verbose_name='车辆细节图')
    index = models.IntegerField(verbose_name='顺序')
    car_detail = models.ForeignKey('CarDetail',verbose_name='车辆细节图')
    class Meta:
        verbose_name = '车辆图片细节'
        verbose_name_plural = verbose_name
class IndexBanner(models.Model):
    models.ImageField(upload_to='/banner',verbose_name='图片')
    index = models.IntegerField(verbose_name='展示顺序')
    class Meta:
        verbose_name = '首页轮播图'
        verbose_name_plural = verbose_name
# Create your models here.
