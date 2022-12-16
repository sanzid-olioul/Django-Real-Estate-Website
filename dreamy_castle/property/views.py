from django.shortcuts import render
from django.views import View
# Create your views here.
class Property(View):
    def get(self,request,*args, **kwargs):
        return render(request,'property.html')

class PropertySingle(View):
    def get(self,request,*args, **kwargs):
        return render(request,'property-single.html')