from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import time
# Create your models here.

def user_directory_path(instance, filename):
    #user images path desider
    user_name = str(instance)[:-8]
    timestap = int(time.time()*1000)
    _,ext = filename.split('.')
    f_name = user_name + str(timestap)+'.'+ext
    return f'agents/{user_name}/{f_name}'

class AgentProfile(models.Model):
    user = models.OneToOneField(User,primary_key=True,on_delete = models.CASCADE)
    profile_photo = models.ImageField(upload_to=user_directory_path,default = 'logo/profile.png')
    about = models.TextField()
    phone = models.CharField(max_length=14)
    mobile = models.CharField(max_length=14)
    facebook = models.URLField(max_length=150)
    twitter =  models.URLField(max_length=150)
    instagram = models.URLField(max_length=150)
    linkedin = models.URLField(max_length=150)

    def __str__(self):
        return f'{self.user.username} Profile'
    

    def save(self,*args, **kwargs):
        try:
            prev = AgentProfile.objects.get(id=self.id)
            if prev.profile_photo != self.profile_photo:
                import os
                if os.path.exists(prev.profile_photo.path):
                    print(prev.profile_photo.name)
                    os.remove(prev.profile_photo.path)
        except:
            pass
        finally:
            super().save(*args, **kwargs)
            p_p = Image.open(self.profile_photo)
            # cp_w ,cp_h = c_p.size
            # pp_w ,pp_h = p_p.size
            p_p.resize((800,896),Image.NEAREST)
            p_p.save(self.profile_photo.path)
    
    