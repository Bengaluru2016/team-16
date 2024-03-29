# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-10 01:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Borrower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Amount_required', models.FloatField()),
                ('Amount_raised', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='investment_track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_invested', models.FloatField()),
                ('date_invested', models.DateField()),
                ('time_invested', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Investor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_invested', models.FloatField()),
                ('amount_returned', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='return_payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('amount', models.FloatField()),
                ('borrower_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Forum.Borrower')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('amount', models.FloatField()),
                ('interest', models.FloatField()),
                ('borrower_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Forum.Borrower')),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=16)),
                ('phoneNumber', models.CharField(max_length=12)),
                ('user_email', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='transaction',
            name='investor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Forum.user'),
        ),
        migrations.AddField(
            model_name='return_payment',
            name='investor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Forum.user'),
        ),
        migrations.AddField(
            model_name='investor',
            name='investor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Forum.user'),
        ),
        migrations.AddField(
            model_name='investment_track',
            name='investor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Forum.user'),
        ),
        migrations.AddField(
            model_name='borrower',
            name='borrower_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Forum.user'),
        ),
    ]
