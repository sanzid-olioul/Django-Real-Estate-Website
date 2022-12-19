from django.contrib import admin
from .models import AgentProfile,Messages
# Register your models here.
# admin.site.register(AgentProfile)
admin.site.register(Messages)
@admin.register(AgentProfile)
class AgentProfileAdmin(admin.ModelAdmin):
    list_display = ('user','profile_photo','phone','mobile','facebook')