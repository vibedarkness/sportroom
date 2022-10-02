from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required()
def gerant_home(request):
    return render(request,"gerant/index.html")

