from django.urls import path
from .views import Property,PropertySingle
urlpatterns = [
    path('',Property.as_view(),name='property'),
    path('<int:id>',PropertySingle.as_view(),name='property-single'),
]
