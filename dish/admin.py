from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Dish


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'tag', 'price')
    list_editable = ('name', 'description', 'tag', 'price')

