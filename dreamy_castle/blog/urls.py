from django.urls import path
from .views import Blog,BlogSingle
urlpatterns = [
    path('',Blog.as_view(),name='blog'),
    path('<int:id>',BlogSingle.as_view(),name='blog-single'),
]
