from django.shortcuts import render, redirect
from .models import *
 

# Create your views here.

#TeamMainPage
def Teammain(request):
    teamdata = Team.objects.all()
    return render(request, 'team/teamindex.html', {'teamdata':teamdata})


#TeamDetail
def Teamdetail(request, slug):
    try:
        teamdata = Team.objects.get(code = slug)
        if teamdata != None:
            return render(request, 'team/teamdetail.html', {'teamdata':teamdata})
    except:
        return redirect('/')
