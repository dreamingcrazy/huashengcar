from django.shortcuts import render,redirect
import re
from apps.user.models import UserInfo
from django.views.generic import View
from django.core.mail import send_mail
from itsdangerous import TimedJSONWebSignatureSerializer as tr
from django.http import HttpResponse
from django.conf import settings
from django.core.urlresolvers import reverse
from celery_tasks.tasks import send_email_celery
from django.contrib.auth import authenticate,login

# Create your views here.
def register(request):
    '''校验请求方式，进入不同的处理函数'''
    if request.method=='GET':
        return render(request,'index.html')

    elif request.method == 'POST':
        # 2、获取前端页面的数据
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        emai = request.POST.get('email')
        # 2.1 判断数据是否为空
        if not all([user_name,password,cpassword,emai]):
            return render(request, 'index.html')


        # 2.2判断邮箱是否符合规范
        if not re.match(r'^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+((\.[a-zA-Z0-9_-]{2,3}){1,2})$',emai):

            return render(request, 'index.html',{'errmsg':'邮箱不符合规范'})

        # 2.3判断重复的操作
        # 2.3.1判断邮箱
        try:
            print('进入try')
            user = UserInfo.objects.filter(email__exact=emai)
            print(user)

        except Exception as e:
            user = None

        if user:
            return render(request, 'index.html', {'errmsg': '邮箱已经被使用'})



        # 2.3.2 判断用户名
        try:
            user = UserInfo.objects.get(username=user_name)
        except Exception as e:
            user = None
        if user:
            return render(request, 'index.html', {'errmsg': '用户名已经被使用'})

        #3.1 创建一个用户对象
        user = UserInfo.objects.create_user(username=user_name,email=emai,password=password)
        # create_user(self, username, email=None, password=None,
        # 3.2 将激活标志设置未0
        user.is_active = 0
        # 3.3 将用户对象保存到数据库中
        user.save()
        print('提交成功')

        return render(request,'index.html')


class RegisterView(View):
    def get(self,request):
        return render(request, 'index.html')

    def post(self,request):
        # 2、获取前端页面的数据
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        email = request.POST.get('email')
        print(email)
        # 2.1 判断数据是否为空
        if not all([user_name, password, cpassword, email]):
            return render(request, 'index.html')

        # 2.2判断邮箱是否符合规范
        if not re.match(r'^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+((\.[a-zA-Z0-9_-]{2,3}){1,2})$', email):
            return render(request, 'index.html', {'errmsg': '邮箱不符合规范'})

        # 2.3判断重复的操作
        # 2.3.1判断邮箱
        # try:
        #     print('进入try')
        #     user = UserInfo.objects.filter(email__exact=email)
        #     print(user)
        #
        # except Exception as e:
        #     user = None
        #
        # if user:
        #     return render(request, 'index.html', {'errmsg': '邮箱已经被使用'})

        # 2.3.2 判断用户名
        try:
            user = UserInfo.objects.get(username=user_name)
        except Exception as e:
            user = None
        if user:
            return render(request, 'index.html', {'errmsg': '用户名已经被使用'})

        # 3.1 创建一个用户对象
        user = UserInfo.objects.create_user(username=user_name, email=email, password=password)
        # create_user(self, username, email=None, password=None,
        # 3.2 将激活标志设置未0
        user.is_active = 0
        # 3.3 将用户对象保存到数据库中
        user.save()
        print('提交成功')



        # 授权码 xiameimei123
        # 4\设置激活链接，并对关键信息进行加密操作
        # 4.0加密
        # 设置秘钥
        # SECRET_KEY = 'fkku7vj#x(o@ilr_u(jzh20q@lyi522%!0)qpg0_p0e2^xw49&'

        t = tr(settings.SECRET_KEY,3600)
        # def __init__(self, secret_key, expires_in=None, **kwargs):

        user_id_dict = {'user_id':user.id}

        active_id = t.dumps(user_id_dict)
        # dumps(self, obj, salt=None, header_fields=None)
        active_id = active_id.decode()

        send_email_celery(to_email=email,active_id=active_id)


        # subject = '花生二手车交易平台'
        # message = ''
        # from_email = 'xiameimei_win@163.com'
        # recipient_list = ['xiameimei_win@163.com']
        # html_message = '<div><a href="http://127.0.0.1:8000/user/active/%s">这是激活邮件</a></div>'%active_id
        #
        # send_mail(subject=subject,message=message,from_email=from_email,recipient_list=recipient_list,html_message=html_message)


        # def send_mail(subject, message, from_email, recipient_list,
        #               fail_silently=False, auth_user=None, auth_password=None,
        #               connection=None, html_message=None):

        return redirect(reverse('car:index'))


class ActiveHandler(View):
    def get(self,request,obj):
        # UserInfo.objects.get(id=user_id)
        print(request)
        print(obj)
        # SECRET_KEY = 'fkku7vj#x(o@ilr_u(jzh20q@lyi522%!0)qpg0_p0e2^xw49&'

        t = tr(settings.SECRET_KEY, 3600)
        try:
            user_id = t.loads(obj)
            userid = user_id['user_id']
            user = UserInfo.objects.get(id=userid)
            user.is_active = 1
            user.save()
            return render(request,'index.html')
        except Exception as e:
            return HttpResponse('激活失败，请充值')



class LoginView(View):
    def get(self,request):
        return HttpResponse('ok')

    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        if not all([username,password]):
            return redirect(reverse('car:index'))

        # 登陆验证
        user = authenticate(username=username,password=password)
        print('哈哈哈')
        print(user.password)
        return HttpResponse('ok')

