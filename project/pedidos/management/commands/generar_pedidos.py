import random
from django.core.management.base import BaseCommand
from rapihogar.models import Technician, User, Scheme
from pedidos.models import Pedido
from django.core.management import call_command
from ...utils.pedidos_list import pedidos_list
from ...utils.location_list import CiudadesCordoba


class Command(BaseCommand):
    help = "Genera N pedidos aleatorios"

    def handle(self, *args, **options):
        cantidad_pedidos = int(
            input("Ingrese el número de pedidos a generar (entre 1 y 100): ")
        )

        if not Technician.objects.exists() or not User.objects.exists():
            # comodidad para el desarrollo
            crear_usuarios_tecnicos = input(
                "No hay técnicos o usuarios registrados. ¿Quieres crear usuarios y técnicos aleatorios? (s/n): "
            )
            if crear_usuarios_tecnicos.lower() == "s":
                try:
                    num_usuarios = int(
                        input("Ingrese la cantidad de usuarios a crear: ")
                    )
                    num_tecnicos = int(
                        input("Ingrese la cantidad de técnicos a crear: ")
                    )

                    if 0 < num_usuarios <= 100 and 0 < num_tecnicos <= 100:
                        call_command("create_random_users", str(num_usuarios))
                        call_command("create_random_technicians", str(num_tecnicos))
                    else:
                        self.stdout.write(
                            self.style.ERROR(
                                "Ingrese números entre 1 y 100 para usuarios y técnicos."
                            )
                        )

                except ValueError:
                    self.stdout.write(
                        self.style.ERROR(
                            "Ingrese números válidos para usuarios y técnicos."
                        )
                    )

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
                work = random.choice(pedidos_list)
                location = random.choice(list(CiudadesCordoba)).value

                Pedido.objects.create(
                    client=client,
                    hours_worked=hours_worked,
                    technician=technician,
                    type_request=Pedido.PEDIDO,
                    title=work.title,
                    description=work.description,
                    location=location,
                    status="Pendiente",
                    scheme=Scheme.objects.first(),  # Adjust this according to your needs
                )

                # Actualiza las horas trabajadas del técnico
                technician.hours_worked += hours_worked
                technician.update_totals()
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
