from django.db import models
from multiselectfield import MultiSelectField
from PIL import Image
import time
from agent.models import AgentProfile

# Create your models here.
AMENITIES = [
    ('balcony','Balcony'),
    ('outdoor-kitchen','Outdoor Kitchen'),
    ('cable-tv','Cable Tv'),
    ('deck','Deck'),
    ('tennis-courts','Tennis Courts'),
    ('internet','Internet'),
    ('parking','Parking'),
    ('sun-room','Sun Room'),
    ('concrete-flooring','Concrete Flooring'),
]
PROPERTY_TYPE = [
    ('house','House'),
    ('hotel','Hotel'),
    ('resturent','Resturent'),
]
STATUS = [
    ('rent','Rent'),
    ('sell','Sell'),
]
def floor_plan_directory_path(instance, filename):
    #user images path desider
    name = str(instance)
    timestap = int(time.time()*1000)
    _,ext = filename.split('.')
    f_name = name + str(timestap)+'.'+ext
    return f'property/{name}/{f_name}'

class Property(models.Model):
    property_name = models.CharField(max_length=35)
    locations = models.CharField(max_length=50)
    property_description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    property_type = models.CharField(max_length=10,choices=PROPERTY_TYPE)
    agent = models.ForeignKey(AgentProfile,on_delete=models.CASCADE)
    status =  models.CharField(max_length=10,choices=STATUS)
    amenities = MultiSelectField(max_length=250,choices=AMENITIES)
    area = models.DecimalField(max_digits=7,decimal_places=2)
    number_of_bed = models.IntegerField()
    number_of_bath = models.IntegerField()
    number_of_garage = models.IntegerField()
    floor_plan = models.ImageField(upload_to=floor_plan_directory_path,null=True,blank=True)
    video_url = models.URLField(max_length=150)
    latitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    longitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    def __str__(self):
        return self.property_name


def property_directory_path(instance, filename):
    #user images path desider
    name = str(instance)
    timestap = int(time.time()*1000)
    _,ext = filename.split('.')
    f_name = name + str(timestap)+'.'+ext
    return f'property/{name}/{f_name}'


class PropertyImages(models.Model):
    image = models.ImageField(upload_to=property_directory_path,default='img\property-1.jpg')
    alt = models.CharField(max_length=50)
    property = models.ForeignKey(Property,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return 'propertyimage'

    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)
        p_p = Image.open(self.image)
        p_p.resize((1920,960),Image.NEAREST)
        p_p.save(self.image.path)