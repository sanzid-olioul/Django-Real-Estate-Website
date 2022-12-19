from django.shortcuts import render
from django.views import View
from .models import Property,PropertyImages
from agent.models import AgentProfile,Messages
from django.http import HttpResponseRedirect
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
    
    def post(self,request,*args, **kwargs):
        property_id = kwargs['id']
        property = Property.objects.get(id = property_id)
        message = Messages()
        message.sender_name = request.POST.get('name','Unknown')
        message.sender_email = request.POST.get('email','unknown@unknown.com')
        message.agent = property.agent.user
        message.message = request.POST.get('message','unknown message')
        message.property_id = property
        message.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        