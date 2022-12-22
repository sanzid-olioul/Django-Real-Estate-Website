from django.contrib import admin
from .models import AboutUs,ContactUs,AllSocialLink
# Register your models here.
@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ['established_on','ceo']


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['location','latitude','longitude']

@admin.register(AllSocialLink)
class AllSocialLinkAdmin(admin.ModelAdmin):
    list_display = ['mail','phone','facebook']