from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("",views.home,name='home'),
    path("logIn",views.logIn,name='logIn'),
    path("signup",views.signup,name='signup'),
    path('createacc',views.createacc,name='createacc'),
    path('forgetpass',views.forgetpass,name='forgetpass'),
    path('varification1',views.varification1,name='varification1'),
    path('varification2', views.varification2, name='varification2'),
    path("logOut", views.logOut, name="logOut"),
    path("change_pass",views.change_pass,name="change_pass")

]
