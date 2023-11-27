import random
from django.core.management.base import BaseCommand
from rapihogar.models import User

class Command(BaseCommand):
    help = 'Crea N usuarios aleatorios'

    def add_arguments(self, parser):
        parser.add_argument('cantidad_usuarios', type=int, help='Número de usuarios a crear')

    def handle(self, *args, **options):
        cantidad_usuarios = options['cantidad_usuarios']

        for _ in range(cantidad_usuarios):
            User.objects.create(
                email=f'usuario{_ + 1}@example.com',
                username=f'usuario{_ + 1}',
                first_name=f'Nombre{_ + 1}',
                last_name=f'Apellido{_ + 1}',
                whatsapp_phone=f'+54{random.randint(100000000, 999999999)}',
                is_active=True,
                is_staff=False,
            )

        self.stdout.write(self.style.SUCCESS(f'Se crearon {cantidad_usuarios} usuarios correctamente'))