from __future__ import unicode_literals

from django.db import models

# Create your models here.

class user(models.Model):
    name=models.CharField(max_length=64)
    password=models.CharField(max_length=16)
    phoneNumber=models.CharField(max_length=12)
    user_email=models.CharField(max_length=32)

class Investor(models.Model):
    investor_id=models.ForeignKey(user)
    amount_invested=models.FloatField()
    amount_returned=models.FloatField()

class Borrower(models.Model):
    borrower_id=models.ForeignKey(user)
    Amount_required=models.FloatField()
    Amount_raised=models.FloatField()
    
class Transaction(models.Model):
    investor_id=models.ForeignKey(user)
    borrower_id=models.ForeignKey(Borrower)
    date=models.DateField()
    time=models.TimeField()
    amount=models.FloatField()
    interest=models.FloatField()

class return_payment(models.Model):
    investor_id = models.ForeignKey(user)
    borrower_id = models.ForeignKey(Borrower)
    date = models.DateField()
    time = models.TimeField()
    amount = models.FloatField()


class investment_track(models.Model):
    investor_id=models.ForeignKey(user)
    amount_invested=models.FloatField()
    date_invested=models.DateField()
    time_invested=models.TimeField()

class Answers(models.Model):
    answer=models.TextField()
