from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
from backend.models import Investor, investment_track, user


def create_pieChart(request,investorId):
    c=Investor.objects.all().filter(Investor_Id=investorId);
    print c;
import pygal
def graph(request,investorId):
    l1 = []
    marks = investment_track.objects.values_list('amount_invested').filter(investor_id=user.objects.get(id=investorId))
    print marks
    for rows in marks:
        print rows
        l1.append(rows[0])
    line_chart = pygal.Line()
    line_chart.add("investment",l1)
    line_chart.render_to_file('graph.svg')
