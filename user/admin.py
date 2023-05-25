from django.contrib import admin
from .models import User


@admin.register(User)
class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'phone_number')
