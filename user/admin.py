from django.contrib import admin

from user.models import UserInfo,UserAddress
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['id','password','is_delete','is_active']
class UserAddressAdmin(admin.ModelAdmin):
    list_display = ['recv','recv_phone','service_phone','address','is_delete']

admin.site.register(UserInfo,UserInfoAdmin)
admin.site.register(UserAddress)
# Register your models here.
