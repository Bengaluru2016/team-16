
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader
from backend.models import Investor, investment_track, user, return_payment
# here i used pygal library to generate plots and save it locally
import pygal
#python method to generate graph plot
def graph(request,investorId):
    l1 = []
    l2=[]
    marks = investment_track.objects.values_list('amount_invested').filter(investor_id=user.objects.get(id='1'))
    print marks
    #we can have time interval vs amount  plot
    for rows in marks:
        print rows
        l1.append(rows[0])
    line_chart = pygal.Line()
    # add functiion name for plot and list of variables to genrate plot
    line_chart.add("investment",l1)
    marks=return_payment.objects.values_list(('amount')).filter(investor_id_id=user.objects.get(id='1'))
    print marks
    for rows in marks:
        print rows
        l2.append(rows[0])
        print l2
    line_chart.add("return", l2)
    line_chart.render_to_file('backend/static/graph.svg')
    # here we are rendering a template to generate html code  which can be shared via facebook on their respective timelines
    temp = loader.get_template("fb_share.html");
    marks2=user.objects.values(('name')).filter(id=investorId)
    marks=Investor.objects.values(('amount_invested')).filter(investor_id_id=user.objects.get(id='3'))
    l1=marks
    l2=marks2
    print l1,l2
    result = temp.render(context={"name2":marks2,"investoramt":marks})
    return HttpResponse(result)
