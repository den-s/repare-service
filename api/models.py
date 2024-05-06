import datetime
from django.db import models
from users.models import User
from django.utils.translation import gettext as _


class OrderStatus(models.Model):
    name = models.CharField(_("status"), max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


class DeviceType(models.Model):
    name = models.CharField("type", max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


class Brand(models.Model):
    name = models.CharField("brand", max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


class Device(models.Model):
    device_type = models.ForeignKey(
        "DeviceType",
        null=True,
        on_delete=models.SET_NULL,
    )
    brand = models.ForeignKey(
        "Brand",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    model = models.CharField("model", max_length=50, null=True, blank=True)
    serial = models.CharField("serial", max_length=50, null=True, blank=True)
    imei = models.CharField("imei", max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.device_type} ({self.brand} {self.model})"


class ReplacementPart(models.Model):
    name = models.CharField("model", max_length=50, null=True, blank=True)
    price = models.PositiveSmallIntegerField()
    delivery_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f"{self.name} ({self.price}грн.) - {self.delivery_date}"


class Order(models.Model):
    date = models.DateField(default=datetime.date.today)
    date_release = models.DateField(default=datetime.date.today)
    date_done = models.DateField()
    status = models.ForeignKey(
        "OrderStatus",
        null=True,
        blank=True,
        verbose_name=_("status"),
        on_delete=models.SET_NULL,
    )
    replacement_parts = models.ManyToManyField(
        "ReplacementPart",
        blank=True,
    )
    client = models.ForeignKey(
        User,
        null=True,
        blank=True,
        related_name="client",
        on_delete=models.SET_NULL,
    )
    worker = models.ForeignKey(
        User,
        null=True,
        blank=True,
        related_name="worker",
        on_delete=models.SET_NULL,
    )
    receiver = models.ForeignKey(
        User,
        null=True,
        blank=True,
        related_name="receiver",
        on_delete=models.SET_NULL,
    )
    device = models.ForeignKey(
        "Device",
        null=True,
        blank=True,
        related_name="device",
        on_delete=models.SET_NULL,
    )
    contents = models.CharField(
        "contents",
        max_length=255,
        null=True,
        blank=True,
    )
    bug = models.CharField(
        "bug",
        max_length=255,
        null=True,
        blank=True,
    )
    notes = models.CharField(
        "notes",
        max_length=255,
        null=True,
        blank=True,
    )
    work_list = models.CharField(
        "actions",
        max_length=255,
        null=True,
        blank=True,
    )
    points_achieved = models.PositiveSmallIntegerField(null=True, blank=True)
    price = models.PositiveSmallIntegerField(null=True, blank=True)
