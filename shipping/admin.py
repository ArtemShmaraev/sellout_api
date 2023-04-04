from django.contrib import admin

# Register your models here.
from .models import ProductUnit, UnitBundle, Platform, Formula, AddressInfo, DeliveryType




class ProductUnitAdmin(admin.ModelAdmin):
    list_display = ('product', 'unit_bundle',)


class DeliveryTypeAdmin(admin.ModelAdmin):
    list_display = ('name', )


class PlatformAdmin(admin.ModelAdmin):
    list_display = ('platform', )

class UnitBundleAdmin(admin.ModelAdmin):
    list_display = ('size', )


admin.site.register(ProductUnit, ProductUnitAdmin)
admin.site.register(Platform, PlatformAdmin)
admin.site.register(DeliveryType, DeliveryTypeAdmin)
admin.site.register(UnitBundle, UnitBundleAdmin)
