from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from agent.models import AgentProfile
import datetime
import time

# Create your models here.
class RangeIntegerField(models.IntegerField):
    def __init__(self, *args, **kwargs):
        validators = kwargs.pop("validators", [])
        min_value = kwargs.pop("min_value", None)
        if min_value is not None:
            validators.append(MinValueValidator(min_value))
        max_value = kwargs.pop("max_value", None)
        if max_value is not None:
            validators.append(MaxValueValidator(max_value))
        kwargs["validators"] = validators

        super().__init__(*args, **kwargs)

today = datetime.date.today()
def floor_plan_directory_path(instance, filename):
    #user images path desider
    name = str(instance)
    timestap = int(time.time()*1000)
    _,ext = filename.split('.')
    f_name = name + str(timestap)+'.'+ext
    return f'featured_photo/{name}/{f_name}'

class AboutUs(models.Model):
    established_on = RangeIntegerField(min_value= 1990, max_value = today.year)
    working_fielsd = models.CharField(max_length=250)
    featured_photo = models.ImageField()
    ceo = models.ForeignKey(AgentProfile,blank = True,null=True,on_delete=models.SET_NULL)
    speech = models.TextField()
    def __str__(self):
        return 'About Us'
    
    class Meta:
        verbose_name_plural = 'about us'


class ContactUs(models.Model):
    location = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=22,decimal_places=16)
    longitude = models.DecimalField(max_digits=22,decimal_places=16)

    def __str__(self):
        return self.location

    class Meta:
        verbose_name_plural = 'contact us'
        
class AllSocialLink(models.Model):
    company_name = models.CharField(max_length=50)
    facebook = models.URLField()
    twitter = models.URLField()
    instagram = models.URLField()
    linkedin = models.URLField()
    mail = models.EmailField()
    phone = models.CharField(max_length=14)
    about = models.TextField()

    def __str__(self):
        return self.mail