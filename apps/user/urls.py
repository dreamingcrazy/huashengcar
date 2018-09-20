from django.conf.urls import url,include
from django.contrib import admin
from apps.user.views import *
urlpatterns = [
    # url(r'^register$',register),
    # url(r'^register_post',register_post)
    url(r'^register_post$', RegisterView.as_view(), name='register'),

    url(r'^active/(.*)', ActiveHandler.as_view(), name='active'),

    url(r'^login$', LoginView.as_view(), name='login')

]
