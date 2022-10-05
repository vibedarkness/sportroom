import json
import requests
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render, reverse


from .EmailBackend import EmailBackEnd


# Create your views here.


def login_page(request):
    if request.user.is_authenticated:
        if request.user.user_type == '1':
            return redirect(reverse("admin_home"))
        elif request.user.user_type == '2':
            return redirect(reverse("gerant_home"))
        else:
            return redirect(reverse("client_home"))
    return render(request, 'main_templates/login.html')


def doLogin(request, **kwargs):
    if request.method != 'POST':
        return HttpResponse("<h4>REFUSER</h4>")
    else:
        
        user = EmailBackEnd.authenticate(request, username=request.POST.get('email'), password=request.POST.get('password'))
        if user != None:
            login(request, user)
            if user.user_type == '1':
                return redirect(reverse("admin_home"))
            elif user.user_type == '2':
                return redirect(reverse("gerant_home"))
            else:
                return redirect(reverse("client_home"))
        else:
            messages.error(request, "details Invalide")
            return redirect(reverse("login"))



def logout_user(request):
    if request.user != None:
        logout(request)
    return redirect(reverse("login"))


# @csrf_exempt
# def get_attendance(request):
#     subject_id = request.POST.get('subject')
#     session_id = request.POST.get('session')
#     try:
#         subject = get_object_or_404(Subject, id=subject_id)
#         session = get_object_or_404(Session, id=session_id)
#         attendance = Attendance.objects.filter(subject=subject, session=session)
#         attendance_list = []
#         for attd in attendance:
#             data = {
#                     "id": attd.id,
#                     "attendance_date": str(attd.date),
#                     "session": attd.session.id
#                     }
#             attendance_list.append(data)
#         return JsonResponse(json.dumps(attendance_list), safe=False)
#     except Exception as e:
#         return None
