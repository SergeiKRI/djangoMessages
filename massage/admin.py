from django.contrib import admin

from massage.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'name', 'email', )
    list_filter = ('first_name', 'name', )
    search_fields = ('first_name', 'name', 'email', )
