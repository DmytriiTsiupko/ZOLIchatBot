from django.contrib import admin
from .models import Dish


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'detail_description', 'tag', 'is_vegan', 'spiciness', 'price', 'photo')
    list_editable = ('name', 'description', 'detail_description', 'is_vegan', 'spiciness', 'tag', 'price', 'photo')
