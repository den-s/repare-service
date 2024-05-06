from rest_framework.serializers import ModelSerializer

from api.models import Brand, Device, DeviceType, Order, OrderStatus, ReplacementPart


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = [
            "id",
            "date",
            "date_release",
            "date_done",
            "status",
            "replacement_parts",
            "client",
            "worker",
            "receiver",
            "device",
            "contents",
            "bug",
            "notes",
            "work_list",
            "price",
            "points_achieved",
        ]


class OrderStatusSerializer(ModelSerializer):
    class Meta:
        model = OrderStatus
        fields = ["id", "name"]


class DeviceTypeSerializer(ModelSerializer):
    class Meta:
        model = DeviceType
        fields = ["id", "name"]


class BrandSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = ["id", "name"]


class DeviceSerializer(ModelSerializer):
    class Meta:
        model = Device
        fields = ["id", "device_type", "brand", "model", "serial", "imei"]


class ReplacementPartSerializer(ModelSerializer):
    class Meta:
        model = ReplacementPart
        fields = ["id", "name", "price", "delivery_date"]
