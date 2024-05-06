from django.dispatch import receiver
from django.db import models
from django.core.cache import cache

from api.models import Order


@receiver(models.signals.post_save, sender=Order)
def clear_cache_orders(sender, instance, **kwargs):
    cache.delete("orders")
