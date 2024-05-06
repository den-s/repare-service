from django.urls import path

from .views import (
    OrdersView,
    OrdersStatusView,
    DeviceTypesView,
    BrandsView,
    DevicesView,
    ReplacementPartsView,
)

urlpatterns = [
    path("orders", OrdersView.as_view()),
    path("order/statuses", OrdersStatusView.as_view()),
    path("devices", DevicesView.as_view()),
    path("device/types", DeviceTypesView.as_view()),
    path("device/brands", BrandsView.as_view()),
    path("replacement-parts", ReplacementPartsView.as_view()),
]
