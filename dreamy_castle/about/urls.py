from django.urls import path
from .views import About,Contact
urlpatterns = [
    path('about/',About.as_view(),name='about'),
    path('contact/',Contact.as_view(),name='contact'),
]
