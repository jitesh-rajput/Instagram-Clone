from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("",views.main,name='main'),
    path("go_to_postpage",views.go_to_postpage,name="go_to_postpage"),
    path("addfriend",views.addfriend,name="addfriend"),
    path("/usersearch", views.usersearch, name="usersearch"),
    path("/changeDP", views.changeDP, name="changeDp"),
    path("/changeBio",views.changeBio,name="changeBio"),
    path("/uploadimg",views.uploadimg,name="uploadimg"),
    path('<str:username>', views.userprofile, name='userprofile'),

]
