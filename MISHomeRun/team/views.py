#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from .models import *
 

# Create your views here.

#Team Main Page
def Teammain(request):
    teamdata = Team.objects.all()
    return render(request, 'team/teamindex.html', {'teamdata':teamdata, 'page_title': '球隊資訊',})


#Team Detail
def Teamdetail(request, slug):
    try:
        teamdata = Team.objects.get(code = slug)
        if teamdata != None:
            return render(request, 'team/teamdetail.html', {'teamdata':teamdata, 'page_title': teamdata.name,})
    except:
        return redirect('/')

#Stat Main Page
def Statmain(request):
    teamdata = Team.objects.all()
    return render(request, 'team/Statindex.html', {'teams':teamdata, 'page_title': '球隊戰績',})

#Stat Detail
def Statdetail(request, slug):
#    try:
    statdata = Stat.objects.filter(code = slug)
    teamdata = Team.objects.get(code = slug)
    if statdata != None:
        return render(request, 'team/statdetail.html', {'statdatas':statdata, 'team': teamdata, 'page_title': u'%s戰績' % teamdata.name,})
#    except:
#        return redirect('/')