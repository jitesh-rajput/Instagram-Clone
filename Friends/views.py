from django.shortcuts import render,HttpResponse
from django.contrib.auth.admin import User
from Profile.models import User_Profile
from .models import Friend_request
# Create your views here.


def addfriend(request):
    othuser=User_Profile.objects.get(username=request.user)
    if othuser:
        friend=othuser.friend.all()
        friend=list(friend)
        user =User_Profile.objects.exclude(username=request.user)
        friend_request=Friend_request.objects.filter(from_user=othuser)
        data={
            'friend':friend,
            'user':user,
            friend_request:friend_request,
        }
        return render(request,'Add Friend.html',{'data':data})

def send_request(request,username):
    print(id)
    username=User.objects.get(username=username)
    fr=User_Profile.objects.get(username=username)
    othuser = User_Profile.objects.get(username=request.user)
    othuser.friend.add(fr)
    if othuser:
        friend = othuser.friend.all()
        friend = list(friend)
        user = User_Profile.objects.exclude(username=request.user)
        friend_request = Friend_request.objects.filter(from_user=othuser)
        data = {
            'friend': friend,
            'user': user,
            friend_request: friend_request,
        }
        return render(request, 'Add Friend.html', {'data': data})