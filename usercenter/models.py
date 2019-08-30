from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    face_image=models.CharField(max_length=100,blank=True,verbose_name='用户头像')

    class Meta(AbstractUser.Meta):
        db_table = 'usercenter_user'
     
    


