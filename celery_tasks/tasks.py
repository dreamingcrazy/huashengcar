from celery import Celery
from django.core.mail import send_mail
import os
from django.conf import settings
from celery import task
import time
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","huashengcar.settings")
django.setup()
app = Celery('celery_tasks.tasks',broker='redis://127.0.0.1:6379/5')
@app.task
def send_email_celery(to_email,active_id):
    subject = '花生二手车交易平台'
    message = ''
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [to_email]
    html_message = '<div><a href="http://127.0.0.1:8000/user/active/%s">这是激活邮件</a></div>'%active_id
    send_mail(subject=subject,message=message,from_email = from_email,recipient_list=recipient_list,html_message=html_message)
    time.sleep(50)