from django.shortcuts import render
from .models import AgentProfile
from property.models import Property,PropertyImages
from django.contrib.auth.models import User
from django.views import View

# Create your views here.
class Agent(View):
    def get(self,request,*args, **kwargs):
        agents = AgentProfile.objects.all()
        return render(request,'agents.html',{'agents':agents})

class AgentSingle(View):
    def get(self,request,*args, **kwargs):
        user = User.objects.get(id = kwargs['id'])
        agent = AgentProfile.objects.get(user = user)
        properties = Property.objects.filter(agent = agent)
        property_datas = []
        for property in properties:
            img = PropertyImages.objects.filter(property=property)
            temp = dict()
            if img:
                temp = {
                    'property':property,
                    'image':img[0].image,
                }
                print(temp['image'])
            else:
                temp = {
                    'property':property,
                    'image':'img\property-1.jpg',
                }
            property_datas.append(temp)
        number_of_properties = len(property_datas)
        return render(request,'agent-single.html',{'agent':agent,'properties':property_datas,'number_of_properties':number_of_properties})