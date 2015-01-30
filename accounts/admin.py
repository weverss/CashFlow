from django.contrib import admin
from accounts.models import *

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display  = ('description', 'created_at', 'updated_at')