import random
from django.core.management.base import BaseCommand
from rapihogar.models import Technician, User, Scheme
from pedidos.models import Pedido
from django.core.management import call_command


class Command(BaseCommand):
    help = "Genera N pedidos aleatorios"

    def handle(self, *args, **options):
        cantidad_pedidos = int(input("Ingrese el número de pedidos a generar (entre 1 y 100): "))

        if not Technician.objects.exists() or not User.objects.exists():
            # comodidad para el desarrollo
            crear_usuarios_tecnicos = input(
                "No hay técnicos o usuarios registrados. ¿Quieres crear un usuario y un técnico aleatorio? (s/n): "
            )
            if crear_usuarios_tecnicos.lower() == "s":
                call_command("create_random_users", "1")  # Crea un usuario aleatorio
                call_command(
                    "create_random_technicians", "1"
                )  # Crea un técnico aleatorio
            else:
                self.stdout.write(
                    self.style.ERROR(
                        "No se crearon técnicos o usuarios. Registra al menos un técnico y un usuario antes de generar pedidos."
                    )
                )
                return

        if 1 <= cantidad_pedidos <= 100:
            technicians = Technician.objects.all()
            clients = User.objects.all()

            for _ in range(cantidad_pedidos):
                technician = random.choice(technicians)
                client = random.choice(clients)
                hours_worked = random.randint(1, 10)

                Pedido.objects.create(
                    client=client,
                    hours_worked=hours_worked,
                    type_request=Pedido.PEDIDO,
                    title=f"Título Pedido {_ + 1}",
                    description=f"Descripción Pedido {_ + 1}",
                    location=f"Ubicación Pedido {_ + 1}",
                    status="Pendiente",
                    scheme=Scheme.objects.first(),  # Adjust this according to your needs
                )

                # Actualiza las horas trabajadas del técnico
                technician.hours_worked += hours_worked
                technician.save()

            self.stdout.write(
                self.style.SUCCESS(
                    f"Se generaron {cantidad_pedidos} pedidos correctamente"
                )
            )
        else:
            self.stdout.write(
                self.style.ERROR("La cantidad de pedidos debe estar entre 1 y 100")
            )
