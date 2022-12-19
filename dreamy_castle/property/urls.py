from django.urls import path
from .views import Properties,PropertySingle
urlpatterns = [
    path('',Properties.as_view(),name='property'),
    path('<int:id>',PropertySingle.as_view(),name='property-single'),
]
