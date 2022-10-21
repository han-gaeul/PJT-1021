from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', )

admin.site.register(get_user_model(), UserAdmin)