from django.conf.urls.i18n import urlpatterns
from django.conf.urls import url

from backend import views

urlpatterns=[
    url(r'id/(?P<investorId>[0-9]+)',views.graph),
]