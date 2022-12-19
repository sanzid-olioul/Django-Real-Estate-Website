from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import AgentProfile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    #Auto profile generate signal for Profile model
    if created:
        AgentProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    #Auto profile generate signal for Profile model
    instance.agentprofile.save()
