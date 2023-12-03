from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User_Profile(models.Model):
    user = models.OneToOneField(User, related_name='user_profile', on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='Uploaded/Login_App/Profile_Pics', default='Uploaded/Login_App/default-profile-pic.png')
    
    def __str__(self):
        return str(self.user)
        
        
    class Meta:
        verbose_name = 'User_Profile'
        verbose_name_plural = 'User_Profiles'