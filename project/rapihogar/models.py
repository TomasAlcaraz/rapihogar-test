from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    username = models.CharField(max_length=765, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    whatsapp_phone = models.CharField(
        max_length=1024,
        blank=True,
        null=True,
        db_index=True,
        verbose_name="Telefono WhatsApp (+54)",
    )
    last_name = models.CharField(
        max_length=100,
        null=True,
    )
    first_name = models.CharField(
        max_length=100,
        null=True,
    )

    @property
    def full_name(self):
        return "{} {}".format(
            self.first_name if self.first_name else "",
            self.last_name if self.last_name else "",
        )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "username"]

    objects = UserManager()

    class Meta:
        app_label = "rapihogar"
        verbose_name = _("RapiHogar User")
        verbose_name_plural = _("RapiHogar Users")


class Scheme(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        app_label = "rapihogar"
        verbose_name = _("Esquema de un pedido")
        verbose_name_plural = _("Esquemas de pedidos")


class Company(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=80)
    website = models.CharField(max_length=100)

    class Meta:
        app_label = "rapihogar"
        verbose_name = _("Empresa")
        verbose_name_plural = _("Empresas")

class Technician(models.Model):
    full_name = models.CharField(max_length=255)
    hours_worked = models.IntegerField(default=0)

    def __str__(self):
        return self.full_name

    class Meta:
        app_label = "rapihogar"
        verbose_name = _("Técnicos Schema")
        verbose_name_plural = "Técnicos"