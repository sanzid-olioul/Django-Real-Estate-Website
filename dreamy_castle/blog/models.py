from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from agent.models import AgentProfile
from ckeditor.fields import RichTextField
import time
from PIL import Image
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

class CommentManager(models.Manager):
    def filter_by_instance(self,instance):
        content_type = ContentType.objects.get_for_model(instance.__class__)
        obj_id = instance.id
        return super(CommentManager,self).filter(content_type=content_type,object_id=obj_id)

class Comment(models.Model):
    name = models.CharField(max_length=35)
    email = models.EmailField()
    # website = models.URLField(max_length=50,blank=True,null=True)
    agent = models.ForeignKey(AgentProfile,on_delete=models.CASCADE,null=True,blank=True)
    parent = models.ForeignKey('self',null=True,blank=True,on_delete=models.SET_NULL)
    comment_body = models.TextField()
    timestamp = models.DateField(auto_now_add=True,null=True,blank=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    objects = CommentManager()
    def __str__(self):
        return self.comment_body
    class Meta:
        indexes = [
            models.Index(fields=["content_type", "object_id"]),
        ]
        ordering = ['-timestamp']
    def children(self):
        return Comment.objects.filter(parent = self)
    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        return True


class Blog(models.Model):
    image = models.ImageField(upload_to=blog_directory_path)
    title = models.CharField(max_length=500)
    author = models.ForeignKey(AgentProfile,on_delete=models.CASCADE)
    catagory = models.CharField(max_length=10,choices=CATAGORY)
    created_at = models.DateField(auto_now_add=True)
    content = RichTextField(blank=True,null=True)

    def __str__(self):
        return self.title

    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)
        p_p = Image.open(self.image)
        p_p.resize((1920,960),Image.NEAREST)
        p_p.save(self.image.path)

    @property
    def comments(self):
        return Comment.objects.filter_by_instance(self)

    