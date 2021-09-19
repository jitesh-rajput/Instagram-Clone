from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from Profile.models import User_Profile
from post.models import Post
from datetime import datetime

# Create your views here.
def main(request):
    userpro=User_Profile.objects.get(username=request.user)
    userdata=User.objects.get(username=request.user)
    return render(request, 'index.html', {'userpro': userpro})
    '''data={
        'userpro':userpro,
        'userdata':userdata
    }'''


def profile(request):
    return redirect('/userprofile')

def go_to_postpage(request):
    return redirect('/post')

def addfriend(request):
    return redirect('/Friends')
def usersearch(request):
    if request.method=="POST":
        searchu=request.POST.get('searchuser')
        uexist=User.objects.filter(username=searchu )
        uexist2=User.objects.filter(first_name=searchu)
        print(uexist)
        if uexist :
            user=User_Profile.objects.get(username=uexist[0])
            return render(request, 'search.html', {'user': user})
        elif uexist2:
            user = User_Profile.objects.get(username=uexist2[0])
            return render(request, 'search.html', {'user': user})
        else:
            return HttpResponse(" <h1> No Result Found...!!!!!</h1> ")
    else:
        return HttpResponse("Error 404 ")

def changeDP(request):
    if request.method=="POST":
        print(request.FILES)
        ndp=request.FILES['dp']

        if ndp:
            user=User_Profile.objects.get(username=request.user)
            if user:
                user.dp = ndp
                user.save(update_fields=['dp'])
                return HttpResponse(" <h1>Dp Changed....</h1>")
            else:
                return HttpResponse("Cant Change Dp ")
        else:
            return HttpResponse("Image Not Found")
    else:
        return HttpResponse(" ERROR 404 ")


def uploadimg(request):
    if request.method=="POST":
        img=request.FILES['image']
        print(img)
        cap=request.POST.get('Caption')
        use_=request.user
        data_=datetime.today()
        if img:
            post_obj=Post(image=img,caption=cap,username=use_,date=data_)
            post_obj.save()
            return HttpResponse("<h1> Photo Uploaded...</h1>")
        else:
            return HttpResponse(" Error   ")
    else:
        return HttpResponse(" ERROR 404 ")

def changeBio(request):
    if request.method=="POST":
        nbio_=request.POST.get('nbio')
        print(nbio_)
        if nbio_:
            user=User_Profile.objects.get(username=request.user)
            if user:
                user.bio = nbio_
                user.save(update_fields=['bio'])
                return HttpResponse(" <h1> Bio Changed </h1> ")
            else:
                return HttpResponse("Cant Change Bio")
        else:
            return HttpResponse("Image Not Found")
    else:
        return HttpResponse(" ERROR 404 ")

def userprofile(request,username):
    print("Welocme ",username)
    othuser=User.objects.filter(username=username)
    if othuser:
        user =User_Profile.objects.filter(username=othuser[0])
        if user:
            user = user[0]
            uname = User.objects.get(username=user)
            imgList = get_images(request.user)
            fname = uname.first_name
            lname = uname.last_name
            bio = user.bio
            dp = user.dp
            friend = user.friend.all()
            no_of_friend = len(friend)
            print(friend)
            print(no_of_friend)
            blank = 1
            if imgList:
                blank = 0
            data = {
                'fname': fname,
                'lname': lname,
                'bio': bio,
                'dp': dp,
                'friend': friend,
                'no_of_friend': no_of_friend,
                'imgList': imgList,
                'blank': blank
            }
            return render(request, 'Profile.html', data)

        else:
            messages.error(request, "Use doen't Upload his DP until !!!!!!!!!!!!")
            return render(request, 'index.html')
    else:
        messages.error(request, 'Erro 404 Occured.....')
        return redirect('/main')
def get_images(user):
    post_obj=Post.objects.filter(username=user)
    imgList=[post_obj[i:i+3] for i in range(0,len(post_obj),3)]
    return imgList

