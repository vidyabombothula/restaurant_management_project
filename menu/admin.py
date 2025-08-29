from django.contrib import admin
from .models import Menu,Order

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display=('name','price')
    search_fields=('name')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=('menu_item','quantity','created_at')
    list_filter=('created_at')