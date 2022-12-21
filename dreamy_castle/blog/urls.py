from django.urls import path
from .views import Blog_View,BlogSingle
urlpatterns = [
    path('',Blog_View.as_view(),name='blog'),
    path('<int:id>',BlogSingle.as_view(),name='blog-single'),
]
