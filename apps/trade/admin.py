from django.contrib import admin

# Register your models here.
from apps.trade.models import OrderInfo,OrderCar
admin.site.register(OrderInfo)
admin.site.register(OrderCar)
# Register your models here.
