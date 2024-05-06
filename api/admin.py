from django.contrib import admin
from users.models import User

from .models import (
    DeviceType,
    Order,
    Device,
    OrderStatus,
    Brand,
    ReplacementPart,
)


class UserAdmin(admin.ModelAdmin):
    pass


class BrandAdmin(admin.ModelAdmin):
    pass


class DeviceAdmin(admin.ModelAdmin):
    pass


class OrderStatusAdmin(admin.ModelAdmin):
    pass


class ReplacementPartAdmin(admin.ModelAdmin):
    pass


class DeviceTypeAdmin(admin.ModelAdmin):
    pass


class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "device",
        "status",
        "client",
        "worker",
        "receiver",
        "date",
        "date_release",
        "date_done",
    ]
    list_filter = [
        "device",
        "status",
        "client",
        "worker",
        "receiver",
        "date",
        "date_release",
        "date_done",
    ]
    pass


admin.site.register(User, UserAdmin)
admin.site.register(Device, DeviceAdmin)
admin.site.register(OrderStatus, OrderStatusAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(ReplacementPart, ReplacementPartAdmin)
admin.site.register(DeviceType, DeviceTypeAdmin)

# Register your models here.
