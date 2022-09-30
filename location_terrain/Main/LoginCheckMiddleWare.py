from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


class LoginCheckMiddleWare(MiddlewareMixin):

    def process_view(self,request,view_func,view_args,view_kwargs):
        modulename=view_func.__module__
        user=request.user
        if user.is_authenticated:
            if user.user_type == "1":
                if modulename == "Main.hodviews":
                    pass
                elif modulename == "Main.views":
                    pass
                else:
                    return HttpResponseRedirect(reverse("admin_home"))
            elif user.user_type == "2":
                if modulename == "Main.gerantviews":
                    pass
                elif modulename == "Main.views":
                    pass
                else:
                    return HttpResponseRedirect(reverse("gerant_home"))
            elif user.user_type == "3":
                if modulename == "Main.clientviews":
                    pass
                elif modulename == "Main.views":
                    pass
                else:
                    return HttpResponseRedirect(reverse("client_home"))
            else:
                return HttpResponseRedirect(reverse("login"))

        else:
            if request.path == reverse("login") or request.path == reverse("do_login"):
                pass
            else:
                return HttpResponseRedirect(reverse("login"))