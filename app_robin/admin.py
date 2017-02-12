from django.contrib import admin
from .models import *
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity']
    list_editable = ['quantity']
    list_filter = ['supermercado']

admin.site.register(newCustomer)
admin.site.register(newProduct, ProductAdmin)
