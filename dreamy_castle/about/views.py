from django.shortcuts import render
from django.views import View
# Create your views here.
class About(View):
    def get(self,request,*args, **kwargs):
        return render(request,'about.html')

class Contact(View):
    def get(self,request,*args, **kwargs):
        return render(request,'contact.html')
