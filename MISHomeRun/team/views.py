from django.shortcuts import render
from .models import *
 

# Create your views here.

#Team Main Page
def Teammain(request):
    teamdata = Team.objects.all()
    return render(request, 'team/teamindex.html', {'teamdata':teamdata})


#Team Detail
def Teamdetail(request, slug):
    try:
        teamdata = Team.objects.get(code = slug)
        if teamdata != None:
            return render(request, 'team/teamdetail.html', {'teamdata':teamdata})
    except:
        return redirect('/')

#Stat Main Page
def Statmain(request):
    teamdata = Team.objects.all()
    return render(request, 'team/Statindex.html', {'teams':teamdata})

#Stat Detail
def Statdetail(request, slug):
#    try:
    statdata = Stat.objects.filter(code = slug)
    teamdata = Team.objects.get(code = slug)
    if statdata != None:
        return render(request, 'team/statdetail.html', {'statdatas':statdata, 'team': teamdata})
#    except:
#        return redirect('/')