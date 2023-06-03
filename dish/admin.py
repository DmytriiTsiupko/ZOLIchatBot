from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Dish


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'tag', 'is_vegan', 'spiciness', 'price')
    list_editable = ('name', 'description', 'is_vegan', 'spiciness', 'tag', 'price')

