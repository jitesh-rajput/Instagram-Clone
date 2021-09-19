from django.db import models
from django.contrib.auth.models import User
from Profile.models import User_Profile

# Create your models here.

class Friend_request(models.Model):
    to_user=models.ManyToManyField(User_Profile,related_name='to_user')
    from_user=models.ManyToManyField(User_Profile,related_name='from_user')
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "From"+str(self.to_user)+"TO"+str(self.from_user)