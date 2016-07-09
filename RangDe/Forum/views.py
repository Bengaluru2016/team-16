import os
import urllib
from django.core.wsgi import get_wsgi_application
from django.core.mail import EmailMultiAlternatives
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "classproject2.settings")
application = get_wsgi_application()
import Forum.models
from Forum.models import *
from django.template import loader
from django.db.models import Count, Avg,Max,Min
import click
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from django.shortcuts import render
from Forum.models import *
import MySQLdb

def mail(request):
    return render(request, 'email.html')

def send_email(request):
    import smtplib
    fromaddr = 'srujanbelde18@gmail.com'
    toaddrs = request.POST['mail']
    name=request.POST['name']
    us=user(name=name,password='abcd',user_email=toaddrs,phoneNumber='12234')
    us.save()
    inv=Investor(investor_id=us,amount_invested=0,amount_returned=100)
    inv.save()
    msg = MIMEText("http://127.0.0.1:8000/new/")
    msg['Subject'] = 'subject'
    msg['From'] = 'xxx'
    msg['To'] = 'xxx'
    username = 'srujanbelde18@gmail.com'
    password = 'xxxx1234XXXX'
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username, password)
        server.sendmail(fromaddr, toaddrs, msg.as_string())
        server.quit()
    except Exception as e:
        print e
    return render(request, 'success.html')