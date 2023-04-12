from django.contrib import admin
from contact.models import *

class ContactAdmin(admin.ModelAdmin):
    list_display=('contact_name','contact_email','contact_subject','contact_message')

admin.site.register(Contact,ContactAdmin)
admin.site.register(news)
admin.site.register(latestNews)

# Register your models here.
