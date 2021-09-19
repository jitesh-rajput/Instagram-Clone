from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [
    path("",views.addfriend,name='addfriend'),
    path("/<str:username>", views.send_request, name="send_request")

]
