from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone =  models.CharField(max_length=15,null=True,blank=True)
    address =  models.CharField(max_length=100,null=True,blank=True)
    
    def __str__(self):
        return self.user.username