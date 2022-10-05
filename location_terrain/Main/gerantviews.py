from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def gerant_home(request):
    return render(request,"gerant/index.html")

@login_required(login_url='/login')
def liste_gerant(request):
    return render(request,"gerant/liste.html")