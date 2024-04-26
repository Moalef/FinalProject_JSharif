from django.contrib import admin
from .models import User,OTPRequest
from django.contrib.auth.admin import UserAdmin


admin.site.register(OTPRequest)
# Register your models here.
@admin.register(User)
class AppUserAdmin(UserAdmin):
    pass