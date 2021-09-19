from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [
    path("",views.postpage,name='postpage'),
    path("/<int:id>",views.showlike,name="showlike"),
    path("/like/<int:id>", views.likepost, name="likepost"),
    path("/addcomment/<int:id>", views.addcomment, name="addcomment"),

]
