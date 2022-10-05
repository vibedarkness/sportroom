from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import GerantForm

from django.shortcuts import (HttpResponse, HttpResponseRedirect,
                              get_object_or_404, redirect, render)
from django.urls import reverse
from .models import CustomUser
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib import messages


@login_required(login_url='/login')
def index(request):
    return render(request, 'hod/index.html')

# @login_required(login_url='/login')
# def liste_gerant(request):
#     return render(request,"hod/liste_gerant.html")

# @login_required(login_url='/login')
# def liste_client(request):
#     return render(request,"hod/liste_client.html")


def add_gerant(request):
    if request.method == "POST":
        form = GerantForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'ajout du gerant reussi')
            return HttpResponseRedirect(reverse("admin_home"))
        else:
            return render(request, "hod/add_gerant.html", {'form': form})
    else:
        form = GerantForm()
        return render(request, "hod/add_gerant.html", {'form': form})
