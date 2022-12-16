from django.shortcuts import render
from django.views import View
# Create your views here.
class Blog(View):
    def get(self,request,*args, **kwargs):
        return render(request,'blog.html')

class BlogSingle(View):
    def get(self,request,*args, **kwargs):
        return render(request,'blog-single.html')