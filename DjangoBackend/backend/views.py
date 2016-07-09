
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader

from backend.models import Investor, investment_track, user, return_payment


def create_pieChart(request,investorId):
    c=Investor.objects.all().filter(Investor_Id=investorId);
    print c;
import pygal
def graph(request,investorId):
    l1 = []
    l2=[]
    marks = investment_track.objects.values_list('amount_invested').filter(investor_id=user.objects.get(id='1'))
    print marks
    for rows in marks:
        print rows
        l1.append(rows[0])
    line_chart = pygal.Line()
    line_chart.add("investment",l1)
    marks=return_payment.objects.values_list(('amount')).filter(investor_id_id=user.objects.get(id='1'))
    print marks
    for rows in marks:
        print rows
        l2.append(rows[0])
        print l2
    line_chart.add("return", l2)
    line_chart.render_to_file('backend/static/graph.svg')
    temp = loader.get_template("fb_share.html");
    marks2=user.objects.values_list(('name')).filter(id=investorId)
    marks=Investor.objects.values_list(('amount_invested')).filter(investor_id_id=user.objects.get(id='3'))
    print marks,marks2
    result = temp.render(context={"name2":marks2})
    return HttpResponse(result)
