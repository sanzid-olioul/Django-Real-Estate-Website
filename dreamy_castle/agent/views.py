from django.shortcuts import render

# Create your views here.
from django.views import View
# Create your views here.
class Agent(View):
    def get(self,request,*args, **kwargs):
        return render(request,'agents.html')

class AgentSingle(View):
    def get(self,request,*args, **kwargs):
        return render(request,'agent-single.html')