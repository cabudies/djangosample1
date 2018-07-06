from django.contrib import admin

from .models import Menu


# Register your models here.

class MenuDetailsAdmin(admin.ModelAdmin):
    list_display = ('recipe_name', 'menucategory', 'price', 'items_in_stock')
    list_filter = ['price', 'menucategory']

admin.site.register(Menu, MenuDetailsAdmin)
