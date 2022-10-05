from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def index(request):
    return render(request,'hod/index.html')

@login_required(login_url='/login')
def liste_gerant(request):
    return render(request,"hod/liste_gerant.html")

@login_required(login_url='/login')
def liste_client(request):
    return render(request,"hod/liste_client.html")