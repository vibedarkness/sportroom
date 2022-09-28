from django.urls import path
from . import views,hodviews

urlpatterns = [
    path('login', views.login,name="login"),

    #hod urls
    path('index', hodviews.index,name="admin_index"),

    # gerant urls
    #client urls
]
