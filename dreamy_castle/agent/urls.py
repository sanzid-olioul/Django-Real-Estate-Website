from django.urls import path
from .views import Agent,AgentSingle
urlpatterns = [
    path('',Agent.as_view(),name='agents' ),
    path('<int:id>',AgentSingle.as_view(),name='agent-single' ),
]
