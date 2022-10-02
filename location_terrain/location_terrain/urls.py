"""location_terrain URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from location_terrain import settings
from Main import views,hodviews,gerantviews,clientviews


urlpatterns = [
    # path('admin/', admin.site.urls),
    #login urls
    path('login', views.login_vibe,name="login"),
    path('logout_user', views.logout_user,name="logout"),
    path('doLogin',views.doLogin,name="do_login"),

    #hod urls
    path('admin/', hodviews.index,name="admin_home"),
    path('liste_gerant', hodviews.liste_gerant,name="liste_gerant"),
    path('liste_client', hodviews.liste_client,name="liste_client"),
    #gerant urls
    path('gerant', gerantviews.gerant_home,name="gerant_home"),
    
    #client urls
    path('', clientviews.client_home,name="client_home"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
