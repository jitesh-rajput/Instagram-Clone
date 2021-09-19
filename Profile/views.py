from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from .models import User_Profile
from django.contrib import messages
from post.models import Post
# Create your views here.


def profile(request):
    othuser=User.objects.filter(username=request.user)
    if othuser:
        user =User_Profile.objects.filter(username=request.user)
        if user :
            user=user[0]
            uname=User.objects.get(username=user)
            imgList=get_images(request.user)
            fname=uname.first_name
            lname=uname.last_name
            friends=user.friends
            bio=user.bio
            dp=user.dp
            blank=1
            if imgList:
                blank=0
            data={
                'fname':fname,
                'lname':lname,
                'friends':friends,
                'bio':bio,
                'dp':dp,
                'imgList':imgList,
                'blank':blank
            }
            return render(request, 'Profile.html', data)

        else:
            messages.error(request,"Use doen't Upload his DP until !!!!!!!!!!!!")
            return render(request,'index.html')
    else:
        messages.error(request,'Erro 404 Occured.....')
        return redirect('/main')

def get_images(user):
    post_obj=Post.objects.filter(username=user)
    imgList=[post_obj[i:i+3] for i in range(0,len(post_obj),3)]
    return imgList

