from django.conf.urls import include,url
from django.contrib import admin
from apps.second_car import views
urlpatterns = [
    url(r'^$',views.index,name='index')
]