from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'unit')


admin.site.register(Product, ProductAdmin)
admin.site.register(Notes)
