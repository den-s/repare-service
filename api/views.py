from django.views import View
from django.http import JsonResponse
from repair_service.decorators import time_logger
from rest_framework.views import Response

from api.models import Brand, Device, DeviceType, Order, OrderStatus, ReplacementPart
from api.serializers import (
    BrandSerializer,
    DeviceSerializer,
    DeviceTypeSerializer,
    OrderSerializer,
    OrderStatusSerializer,
    ReplacementPartSerializer,
)


class OrdersView(View):
    @time_logger
    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return JsonResponse(serializer.data, safe=False)


class OrdersStatusView(View):
    @time_logger
    def get(self, request):
        statuses = OrderStatus.objects.all()
        serializer = OrderStatusSerializer(statuses, many=True)
        data = {item["id"]: dict(item) for item in serializer.data}
        return JsonResponse(data, safe=False)


class DeviceTypesView(View):
    @time_logger
    def get(self, request):
        types = DeviceType.objects.all()
        serializer = DeviceTypeSerializer(types, many=True)
        data = {item["id"]: dict(item) for item in serializer.data}
        return JsonResponse(data, safe=False)


class BrandsView(View):
    @time_logger
    def get(self, request):
        brands = Brand.objects.all()
        serializer = BrandSerializer(brands, many=True)
        data = {item["id"]: dict(item) for item in serializer.data}
        return JsonResponse(data, safe=False)


class DevicesView(View):
    @time_logger
    def get(self, request):
        devices = Device.objects.all()
        serializer = DeviceSerializer(devices, many=True)
        data = {item["id"]: dict(item) for item in serializer.data}
        return JsonResponse(data, safe=False)


class ReplacementPartsView(View):
    @time_logger
    def get(self, request):
        rp = ReplacementPart.objects.all()
        serializer = ReplacementPartSerializer(rp, many=True)
        data = {item["id"]: dict(item) for item in serializer.data}
        return JsonResponse(data)
