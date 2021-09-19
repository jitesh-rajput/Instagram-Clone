from django.db import models 
from django.contrib.auth.models import User
from _datetime import date
# Create your models here.


class Post(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    caption=models.TextField(blank=True)
    image=models.ImageField(upload_to="Post")
    date=models.DateTimeField(auto_now_add=True)
    likes=models.IntegerField(default=0)
    comments=models.IntegerField(default=0)

    def __str__(self):
        return str(self.username)+" "+str(date.today())

class like(models.Model):
    post_id=models.ForeignKey(Post,related_name='post_id',on_delete=models.CASCADE)
    username=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_name")
    def __str__(self):
        return str(self.username)+" Like "+str(self.post_id)

class comment(models.Model):
    post_id=models.ForeignKey(Post,related_name='p_id',on_delete=models.CASCADE)
    uname=models.ForeignKey(User,related_name='uname',on_delete=models.CASCADE)
    comment=models.TextField()
    def __str__(self):
        return str(self.uname)+" comment "+str(self.post_id)