from django.contrib import admin
from .models import ProductMaterial, Warehouse


class ProductMaterialAdmin(admin.ModelAdmin):
    list_display = ("product_name", "fabric", "yarn", "button", "zip")


class WarehouseAdmin(admin.ModelAdmin):
    list_display = ("material_name", "remainder", "price")


admin.site.register(ProductMaterial, ProductMaterialAdmin)
admin.site.register(Warehouse, WarehouseAdmin)
