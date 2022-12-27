from django.contrib import admin
from .models import Client


class ClientAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.register(Client, ClientAdmin)