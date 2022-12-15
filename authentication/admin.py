from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .form import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomerUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomerUser
    list_display = ["email", "username", ]


admin.site.register(CustomerUser, CustomUserAdmin)