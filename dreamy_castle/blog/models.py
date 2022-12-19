from django.db import models
from agent.models import AgentProfile
from ckeditor.fields import RichTextField
from PIL import Image
import time
# Create your models here.

def blog_directory_path(instance, filename):
    #user images path desider
    name = str(instance)
    timestap = int(time.time()*1000)
    _,ext = filename.split('.')
    f_name = name + str(timestap)+'.'+ext
    return f'blogs/{name}/{f_name}'

CATAGORY = [
    ('travel','Travel'),
    ('food','Food'),
    ('it','IT'),
]

class Comment(models.Model):
    name = models.CharField(max_length=35)
    email = models.EmailField()
    website = models.URLField(max_length=50,blank=True,null=True)
    comment = models.TextField()

class CommentReaply(models.Model):
    agent = models.ForeignKey(AgentProfile,on_delete=models.CASCADE)
    reaply = models.TextField()
    comment = models.ForeignKey(Comment,on_delete=models.CASCADE)

class Blog(models.Model):
    image = models.ImageField(upload_to=blog_directory_path)
    title = models.CharField(max_length=500)
    author = models.ForeignKey(AgentProfile,on_delete=models.CASCADE)
    catagory = models.CharField(max_length=10,choices=CATAGORY)
    created_at = models.DateField(auto_now=False, auto_now_add=True)
    content = RichTextField(blank=True,null=True)

    def __str__(self):
        return self.title

    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)
        p_p = Image.open(self.image)
        p_p.resize((1920,960),Image.NEAREST)
        p_p.save(self.image.path)



    