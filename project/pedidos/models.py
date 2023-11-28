from django.db import models
from rapihogar.models import User, Scheme, Technician


# Create your models here.
class Pedido(models.Model):
    SOLICITUD = 0
    PEDIDO = 1

    TIPO_PEDIDO = (
        (SOLICITUD, "Solicitud"),
        (PEDIDO, "Pedido"),
    )
    type_request = models.IntegerField(
        choices=TIPO_PEDIDO, db_index=True, default=PEDIDO
    )
    client = models.ForeignKey(User, verbose_name="cliente", on_delete=models.CASCADE)
    scheme = models.ForeignKey(Scheme, null=True, on_delete=models.CASCADE)
    technician = models.ForeignKey(Technician, on_delete=models.CASCADE)
    hours_worked = models.IntegerField(default=0)

    # new propeties
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    status = models.CharField(max_length=50)

    class Meta:
        app_label = "rapihogar"
        verbose_name = "Pedido"
        ordering = ("-id",)
