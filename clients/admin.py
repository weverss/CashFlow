from django.contrib import admin
from clients.models import *

class PhoneInline(admin.TabularInline):
    model = Phone
    fk = 'client'

class ClientAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display  = ('name',)

    inlines = [
        PhoneInline
    ]

admin.site.register(Client, ClientAdmin)