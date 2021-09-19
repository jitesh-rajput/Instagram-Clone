from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('/<str:username>',views.chat,name="chat"),
    path('sendmsg/<str:username>', views.sendmsg, name="sendmsg"),

]
