from django.shortcuts import render
from django.views import View
from .models import Property,PropertyImages
from agent.models import AgentProfile
# Create your views here.
class Properties(View):
    def get(self,request,*args, **kwargs):
        properties = Property.objects.all()
        return render(request,'property.html',{'properties':properties})

class PropertySingle(View):
    def get(self,request,*args, **kwargs):
        property = Property.objects.get(id=kwargs['id'])
        images = PropertyImages.objects.filter(property = property.id)
        agent = AgentProfile.objects.get(user = property.agent.user)
        return render(request,'property-single.html',{'property':property,'images':images,'agent':agent})