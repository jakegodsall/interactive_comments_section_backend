from django.contrib import admin

from api.models import ProfileImage, Profile, Message

# Register your models here.

admin.site.register(ProfileImage)
admin.site.register(Profile)
admin.site.register(Message)
