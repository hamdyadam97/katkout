from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import gettext_lazy as _
# from rest_framework_simplejwt.token_blacklist.admin import OutstandingTokenAdmin as OldOutstandingTokenAdmin
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken

from .models import User


class UserAdmin(DjangoUserAdmin):
    list_display = ('username', 'email', 'display_name', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'password', 'is_set_password')}),
        (_('Personal info'), {'fields': (
            'display_name', 'email', 'avatar',
        )}),
        ('Email Verification', {'fields': (
            'email_verification_code', 'is_email_verified'
        )}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    search_fields = ('username', 'email', 'display_name', 'phone_number',)

# class OutstandingTokenAdmin(OldOutstandingTokenAdmin):
#     def has_delete_permission(self, *args, **kwargs):
#         return True


# admin.site.unregister(OutstandingToken)

admin.site.register(User, UserAdmin)
# admin.site.register(OutstandingToken, OutstandingTokenAdmin)

