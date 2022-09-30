from django.shortcuts import render
import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect

from django.urls import reverse

from .EmailBackend import EmailBackEnd

# Create your views here.

def login_vibe(request):

    return render(request,'login.html')


def doLogin(request):
    if request.method!="POST":
        return HttpResponse("<h2>Cette n'est pa pris en charge</h2>")
    else:
        user=EmailBackEnd.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        if user is not None:
            login(request,user)
            if user.user_type=="1":
                return HttpResponseRedirect(reverse("admin_home"))
            elif user.user_type=="2":
                return HttpResponseRedirect(reverse("gerant_home"))
            else:
                return HttpResponseRedirect(reverse("client_home"))
        else:
            messages.error(request,"Erreur: Verifier les informations que vous avez saisie")
            return HttpResponseRedirect("/login")


def GetUserDetails(request):
    if request.user!=None:
        return HttpResponse("User : "+request.user.email+" usertype : "+str(request.user.user_type))
    else:
        return HttpResponse("Svp connectez vous d'abord")

def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/login")