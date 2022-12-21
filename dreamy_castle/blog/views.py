from django.shortcuts import render
from django.views import View
from .models import Blog,Comment
# Create your views here.
class Blog_View(View):
    def get(self,request,*args, **kwargs):
        blogs = Blog.objects.all()
        return render(request,'blog.html',{'blogs':blogs})

class BlogSingle(View):
    def get(self,request,*args, **kwargs):
        blog = Blog.objects.get(id=kwargs['id'])
        blog_datas = dict()
        blog_datas['blog'] = blog
        blog_datas['comments'] = []
        comments = Comment.objects.filter_by_instance(blog)
        for comment in comments:
            temp = {
                'comment':comment,
                'reaplies':Comment.objects.filter_by_instance(comment)
            }
            blog_datas['comments'].append(temp)

        return render(request,'blog-single.html',{'blog':blog_datas})