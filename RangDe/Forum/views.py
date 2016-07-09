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


def send_email(request):
    import smtplib
    fromaddr = 'srujanbelde18@gmail.com'
    toaddrs = request.POST['mail']
    name=request.POST['name']
    msg = 'hello Mr'+name+'your friend Mr Srujan has invested into RangDe ' \
                          'and earned rs 50 and he has given that to you to invest to invest into our firm plese' \
                          'accept the following link to do so' \
                          'thankyou :)'
    username = 'srujanbelde18@gmail.com'
    password = 'xxxx1234XXXX'
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username, password)
        server.sendmail(fromaddr, toaddrs, msg)
        server.quit()
        click.echo("successfull sent report")
    except Exception as e:
        print e
        click.echo("not sent")

