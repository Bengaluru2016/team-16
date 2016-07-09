from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
from backend.models import Investor
def create_pieChart(request,investorId):
    c=Investor.objects.all().filter(Investor_Id=investorId);
    print c;
