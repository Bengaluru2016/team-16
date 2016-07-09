from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
from backend.models import Investor
def create_pieChart(request,investorId):
    c=Investor.objects.all().filter(Investor_Id=investorId);
    print c;
import pygal
def graph():
    l1 = []
    l2 = []
    l3 = []
    marks = Investor.objects.values_list('investor_id__name', 'amount_invested')
    for rows in marks:
        l1.append(rows[1])
    bar = pygal.Bar()
    bar.add('minimum', l1)
    bar.add('average', l2)
    bar.add('maximum', l3)
    bar.render_to_file('graph.svg')
    bar.render()
