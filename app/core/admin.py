from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext, gettext_lazy as _

from core.models import User

class UserAdmin(BaseUserAdmin):
    ordering = ["id"]
    list_display = ("email", "password")
    fieldsets= (
        (None,{"fields":("email","password")}),
        (_("Permissions"),{"fields":("is_staff","is_active","is_superuser")}),
        (_("Login Details"),{"fields":("last_login",)}),
    ) 
    readonly_fields = ("last_login",)

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1','password2'),
        }),
    )

admin.site.register(User, UserAdmin)

