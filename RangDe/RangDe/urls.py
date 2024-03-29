"""RangDe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from Forum import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^new/',views.send_email,name='email'),
    url(r'^buck/',views.mail,name='send_email'),
    url(r'^list/',views.Answerslist,name='list'),
    url(r'^list1/',views.insert_answer,name='list1'),
    url(r'^home/',views.home,name='home'),
    url(r'^login/',views.login_check,name='login_insert'),
    url(r'^register/',views.register_upload,name='home'),
    url(r'^login_page/',views.login,name='login_insert'),
    url(r'^graph_page/(?P<investorId>[0-9]+)',views.graph,name='graph_page'),
]
