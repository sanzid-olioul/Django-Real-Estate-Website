from django.contrib import admin
from .models import Blog,Comment,CommentReaply
# Register your models here.
admin.site.register(Comment)
admin.site.register(CommentReaply)
admin.site.register(Blog)
