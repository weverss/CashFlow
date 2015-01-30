from django.contrib import admin
from clients.models import *

class PhoneInline(admin.TabularInline):
    model = Phone
    fk = 'client'
    extra = 1

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display  = ('name', 'created_at', 'updated_at')

    inlines = [
        PhoneInline
    ]