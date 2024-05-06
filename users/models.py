from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _


class User(AbstractUser):
    ROLES = (
        ("worker", _("Worker")),
        ("receiver", _("Receiver")),
        ("client", _("Client")),
    )

    name = models.CharField(_("name"), max_length=50, null=True, blank=True)
    password = models.CharField(_("password"), max_length=255)
    role = models.CharField(_("role"), max_length=20, choices=ROLES, default="worker")
    username = models.CharField(_("email"), max_length=50, unique=True)
    address = models.CharField(_("address"), max_length=250, null=True, blank=True)
    phone = models.CharField(_("phone"), max_length=50, null=True, blank=True)
