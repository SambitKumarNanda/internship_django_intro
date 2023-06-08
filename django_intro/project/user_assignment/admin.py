from django.contrib import admin
from user_assignment.models import UserModel,UserProfileModel,UserPostModel

# Register your models here.

admin.site.register(UserModel)
admin.site.register(UserProfileModel)
admin.site.register(UserPostModel)