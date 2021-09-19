from django.db import models
from django.contrib.auth.models import User
from Friends.models import Friend_request
# Create your models here.

class User_Profile(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    dp=models.ImageField(upload_to="Profile")
    bio=models.CharField(max_length=30,blank=True)
    friend=models.ForeignKey(Friend_request,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.username)

