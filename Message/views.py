from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User,auth
from .models import Message
from Profile.models import User_Profile
import datetime
# Create your views here.

def profile(request):
    othuser=User_Profile.objects.get(username=request.user)
    friends=othuser.friends.all()
    print(friends)
    return render(request,'Message.html')

def chat(request,username):
    s_user=User.objects.get(username=request.user)
    r_user=User.objects.get(username=username)
    all_s  =Message.objects.filter(from_user=s_user,to_user=r_user)|Message.objects.filter(from_user=r_user,to_user=s_user).order_by('time')
    data={
        'user':User.objects.get(username=username),
        'all_message':all_s,
    }
    return render(request,'Message.html',{'data':data})

def sendmsg(request,username):
    if request.method=="POST":
        msg=request.POST.get('msg')
        print(msg)
        s_user=User.objects.get(username=request.user)
        r_user=User.objects.get(username=username)
        message=Message(from_user=s_user,to_user=r_user,message=msg,time=datetime.datetime.today())
        message.save()
        all_s = Message.objects.filter(from_user=s_user, to_user=r_user) | Message.objects.filter(from_user=r_user,
                                                                                                  to_user=s_user).order_by(
            'time')
        data = {
            'user': User.objects.get(username=username),
            'all_message': all_s,
        }
        return render(request, 'Message.html', {'data': data})
    else:
        return HttpResponse("Something Problem..........")
