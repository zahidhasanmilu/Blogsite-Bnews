from django.contrib import admin

# Register your models here.
from .models import User_Profile

# Register your models here.


class User_ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "profile_pic"]


admin.site.register(User_Profile, User_ProfileAdmin)
