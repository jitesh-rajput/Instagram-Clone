from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from Profile.models import User_Profile,User
from post.models import Post,like,comment
# Create your views here.
def postpage(request):
    othuser=User.objects.filter(username=request.user)
    if othuser:
        '''othuser=othuser[0]
        post_obj=User_Profile.objects.get(username=othuser)
        friends=post_obj.friends_name
        if friends:
            print(friends)
            
            data={
                ''
            }'''
        post_obj=Post.objects.all()
        return render(request,'Post.html',{'post':post_obj})
    else:
        HttpResponse("Error 404")

def showlike(request,id):
    like_user=like.objects.filter(post_id=id)
    comment_user=comment.objects.filter(post_id=id)
    post=Post.objects.get(id=id)
    data={
        'comment_user': comment_user,
        'like_user':like_user,
        'post':post
    }
    return render(request,'show.html',{'data':data})

def likepost(request,id):
    post_available=Post.objects.get(id=id)
    print(post_available)
    if post_available:
        check=like.objects.filter(post_id=post_available.id,username=request.user)
        print(check)
        if check:
            return HttpResponseRedirect('/go_to_postpage')
        else:
            like_=like(post_id=post_available,username=request.user)
            like_.save()
            total_like=post_available.likes
            n_likes=total_like+1
            print(n_likes)
            post_available.likes=n_likes
            post_available.save(update_fields=['likes'])
            print(post_available.likes)
            return HttpResponseRedirect('/go_to_postpage')
    else:
        return HttpResponse(" Post Not Available...")


def addcomment(request,id):
    post_available=Post.objects.get(id=id)
    print(post_available)
    if post_available:
        comment_=request.POST.get('comment')
        print(comment_)
        add_=comment(post_id=post_available,uname=request.user,comment=comment_)
        add_.save()
        total_comment=post_available.comments
        n_comments=total_comment+1
        print(n_comments)
        post_available.comments=n_comments
        post_available.save(update_fields=['comments'])
        print(post_available.comments)
        return HttpResponseRedirect('/go_to_postpage')
    else:
        return HttpResponse(" Post Not Available...")